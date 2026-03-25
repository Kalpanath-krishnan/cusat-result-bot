from playwright.sync_api import sync_playwright
import json

REGISTER_NO = "YOUR_REGISTRATION_NUMBER"
BASE_URL = "http://exam.cusat.ac.in/erp5/cusat/Cusat-Home/home_oldresults"


def scrape_all_results():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        all_results = []

        print("Opening OLD RESULTS page...")
        page.goto(BASE_URL)
        page.wait_for_selector("text=Download/View Result")

        links = page.locator("text=Download/View Result")
        total = links.count()

        print(f"Total links found: {total}\n")

        for i in range(total):
            try:
                print(f"\n🔄 Processing result {i+1}/{total}")

                # Re-fetch links (important after navigation)
                links = page.locator("text=Download/View Result")
                if i >= links.count():
                    break

                link = links.nth(i)
                link.scroll_into_view_if_needed()
                link.click()

                # Wait for input
                page.wait_for_selector("input[type='text']", timeout=10000)
                page.fill("input[type='text']", REGISTER_NO)

                # 🔥 Capture new tab
                with context.expect_page() as new_page_info:
                    if page.locator("input[type='submit']").count() > 0:
                        page.locator("input[type='submit']").first.click()
                    elif page.locator("text=Proceed").count() > 0:
                        page.click("text=Proceed")
                    else:
                        page.keyboard.press("Enter")

                result_page = new_page_info.value
                result_page.wait_for_load_state()

                print("   ✅ Result tab opened")

                # 🔥 Extract td
                tds = result_page.locator("td")
                count = tds.count()

                if count == 0:
                    print("   ⚠️ No data found")
                    result_page.close()
                    page.go_back()
                    continue

                row_data = []

                for j in range(count):
                    text = tds.nth(j).text_content()
                    text = text.strip() if text else ""

                    if text:
                        row_data.append(text)

                result_json = {
                    "result_index": i + 1,
                    "register_no": REGISTER_NO,
                    "td_data": row_data
                }

                all_results.append(result_json)

                print(f"   📊 Extracted {len(row_data)} fields")

                # Close result tab
                result_page.close()

                # Go back to list
                page.go_back()
                page.wait_for_load_state()

            except Exception as e:
                print(f"   ❌ Error at result {i+1}: {e}")
                try:
                    page.go_back()
                except:
                    pass
                continue

        # ✅ Final output
        print("\n🔥 ALL RESULTS JSON:\n")
        print(json.dumps(all_results, indent=2))

        # Optional: save
        with open("all_results.json", "w") as f:
            json.dump(all_results, f, indent=2)

        print("\n✅ Saved to all_results.json")

        input("\nPress ENTER to close browser...")


if __name__ == "__main__":
    scrape_all_results()