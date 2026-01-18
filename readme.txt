@"
# 🚀 PriceAPI.pl - Ceny z Allegro (LIVE!)

## 🟢 Endpoint LIVE:
\`GET https://qopylxd8ck.execute-api.eu-west-1.amazonaws.com/prod/prices\`

## 📱 Testuj teraz:
**curl:**
\`\`\`bash
curl https://qopylxd8ck.execute-api.eu-west-1.amazonaws.com/prod/prices
\`\`\`

**Python:**
\`\`\`python
import requests
r = requests.get('https://qopylxd8ck.execute-api.eu-west-1.amazonaws.com/prod/prices')
print(r.json())
\`\`\`

## 📊 Dane LIVE (2026-01-18):
\`\`\`json
{
  \"message\": \"PriceAPI v1 - MVP working\",
  \"count\": 3,
  \"products\": [
    {\"name\": \"Xiaomi Mi Band 7\", \"price\": \"179 PLN\", \"stock\": \"Dostępny\"},
    {\"name\": \"Samsung Galaxy Watch 6\", \"price\": \"899 PLN\", \"stock\": \"Dostępny\"}
  ]
}
\`\`\`

## 💰 Biznes:
- Mock → Allegro OAuth (next)
- API Gateway → Custom domain
- Stripe billing ready

**Kontakt: @malcz (Telegram/Discord)**
"@ | Out-File -FilePath "README.md" -Encoding UTF8
