```markdown
# 🚀 PriceAPI.pl - Ceny Allegro LIVE!

## 📡 Endpoint (API Key required):
```
https://qopylxd8ck.execute-api.eu-west-1.amazonaws.com/prod/prices
```

## 🧪 Testuj (z kluczem API):

**curl:**
```bash
curl -H "x-api-key: YOUR_API_KEY" https://qopylxd8ck.execute-api.eu-west-1.amazonaws.com/prod/prices
```

**Python:**
```python
import requests
headers = {"x-api-key": "YOUR_API_KEY"}
r = requests.get("https://qopylxd8ck.execute-api.eu-west-1.amazonaws.com/prod/prices", headers=headers)
print(r.json())
```

## 📊 Dane LIVE (2026-01-18):
```
Xiaomi Mi Band 7 → 179 PLN (Dostępny) ✅
Samsung Galaxy Watch 6 → 899 PLN ✅
Amazfit GTS 4 → 699 PLN (Brak)  
```

## 💰 Pricing:
```
Pro Plan: 49 PLN/miesiąc = 10k requests/dzień
Enterprise: Kontakt

API Key + billing po Stripe
```

## 📞 Kontakt:
```
Telegram: 
Email: 
```

## 🚀 Deployment:
```
AWS Lambda + API Gateway + Usage Plans
Repo zawiera pełny stack deployment
```
