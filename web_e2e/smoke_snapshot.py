import json
import os
from playwright.sync_api import sync_playwright


def main():
    base_url = os.getenv("BASE_URL", "https://stage.moon.supremainc.com/login")
    out_dir = "/workspace/web_e2e"
    os.makedirs(out_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1366, "height": 900})
        page = context.new_page()
        page.goto(base_url, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)

        # Screenshot
        page.screenshot(path=os.path.join(out_dir, "smoke.png"))

        # DOM content
        html_content = page.content()
        with open(os.path.join(out_dir, "smoke_dom.html"), "w", encoding="utf-8") as f:
            f.write(html_content)

        # Roles snapshot
        roles = page.evaluate(
            """
            () => Array.from(document.querySelectorAll('[role]')).map(el => ({
              role: el.getAttribute('role'),
              name: el.getAttribute('aria-label') || el.innerText.slice(0, 80),
              tag: el.tagName,
              classes: el.className,
              html: el.outerHTML.slice(0, 200)
            }))
            """
        )
        with open(os.path.join(out_dir, "smoke_roles.json"), "w", encoding="utf-8") as f:
            json.dump(roles, f, ensure_ascii=False, indent=2)

        # Inputs snapshot
        inputs = page.evaluate(
            """
            () => Array.from(document.querySelectorAll('input, textarea, [contenteditable=true]')).map(el => ({
              tag: el.tagName,
              type: el.getAttribute('type'),
              placeholder: el.getAttribute('placeholder'),
              name: el.getAttribute('name'),
              id: el.id,
              classes: el.className,
              html: el.outerHTML.slice(0, 200)
            }))
            """
        )
        with open(os.path.join(out_dir, "smoke_inputs.json"), "w", encoding="utf-8") as f:
            json.dump(inputs, f, ensure_ascii=False, indent=2)

        context.close()
        browser.close()


if __name__ == "__main__":
    main()

