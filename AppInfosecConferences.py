import asyncio
import csv
from playwright.async_api import async_playwright

URL = "https://infosec-conferences.com/"

async def safe_inner_text(element):
    try:
        return (await element.inner_text()).strip()
    except Exception:
        return ""

async def scrape_events(output_csv="infosec_conferences.csv"):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL)

        await page.wait_for_selector("table.table-striped tbody tr", timeout=60000)

        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Extraer encabezados
            header_cells = await page.query_selector_all("table.table-striped thead tr th")
            headers = []
            for cell in header_cells:
                text = await safe_inner_text(cell)
                headers.append(text)
            writer.writerow(headers)

            total_events = 0
            total_pages = 0

            while True:
                rows = await page.query_selector_all("table.table-striped tbody tr")
                for row in rows:
                    cols = await row.query_selector_all("td")
                    data = []
                    for col in cols:
                        text = await safe_inner_text(col)
                        data.append(text)
                    writer.writerow(data)
                total_events += len(rows)
                total_pages += 1

                # Intentar ir a la siguiente página
                next_button = await page.query_selector("ul.pagination li.page-item.next:not(.disabled) a")
                if next_button:
                    await next_button.click()
                    await page.wait_for_load_state('networkidle')
                    await page.wait_for_selector("table.table-striped tbody tr", timeout=60000)
                    # Pausa pequeña para evitar saturar
                    await asyncio.sleep(1)
                else:
                    break

            print(f"Scraped {total_events} events over {total_pages} pages.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_events())
