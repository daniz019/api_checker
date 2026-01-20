from app import ApiChecker

urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://google.com",
    "https://url-que-nao-existe.com"
]

for url in urls:
    checker = ApiChecker(url)
    status = checker.check_status()
    
    if isinstance(status, int) and 200 <= status < 300:
        print(f"API Online (Status: {status})")
    else:
        print(f"API Offline ou com Erro (Detalhe: {status})")


