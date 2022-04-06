# Reportcov is maintained at http://localhost:3000/Cov/reportcov
curl -F "data=@tests/index.html" "http://localhost:1111/upload" -H "Authorization: Token ${FLAG}" || true
