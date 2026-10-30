import requests
from bs4 import BeautifulSoup
import csv

url = 'https://realpython.github.io/fake-jobs/'
response = requests.get(url)
print(response)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())  # prints well-formatted HTML

job_cards = soup.select('div.card-content') # mengambil semua elemen job_card

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header CSV
    writer.writerow([
        "Job Title",
        "Company Name",
        "Location",
        "Job URL"
    ])

    # 5. Mengambil data dari setiap kartu
    for job in job_cards:
        title_element = job.select_one("h2.title")
        company_element = job.select_one("h3.company")
        location_element = job.select_one("p.location")

        # Cari link dengan teks "Apply"
        apply_link = job.find(
            "a",
            string=lambda text: text and text.strip() == "Apply"
        )

        # Ekstrak teks dan URL
        title = title_element.get_text(strip=True) if title_element else ""
        company = company_element.get_text(strip=True) if company_element else ""
        location = location_element.get_text(strip=True) if location_element else ""
        job_url = apply_link.get("href", "") if apply_link else ""

        # Tulis satu lowongan ke satu baris CSV
        writer.writerow([
            title,
            company,
            location,
            job_url
        ])

print(f"Berhasil menyimpan {len(job_cards)} lowongan ke jobs.csv")

