 = "https://qopylxd8ck.execute-api.eu-west-1.amazonaws.com/prod/prices"
Write-Host "Testing PriceAPI..." -ForegroundColor Green
try {
     = Invoke-RestMethod -Uri  -Method Get
    Write-Host "✅ API OK! Response:" -ForegroundColor Green
     | ConvertTo-Json -Depth 3
} catch {
    Write-Host "❌ API Error: " -ForegroundColor Red
}
Read-Host "Press Enter to exit"
