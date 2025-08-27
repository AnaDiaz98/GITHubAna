from fastapi import FastAPI
import requests 

app = FastAPI()

def trivia_fetch(num: int):
    """Obtiene 3 trivias sobre el número dado usando la API de Numbers."""
    url = f"http://numbersapi.com/{num}/trivia"
    trivias = []

    for i in range(3):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                trivias.append(response.text)
            else:
                trivias.append(f"Error al obtener trivia {i+1}")
        except requests.exceptions.RequestException as e:
            trivias.append(f"Error de conexión: {e}")

    return {
        "number": num,
        "trivias": trivias
    }

@app.get("/")
def index():
    return {"mensaje": "Hola mundo, usa /trivia/{num} para obtener trivias"}

@app.get("/trivia/{num}")
def get_trivia(num: int):
    """Endpoint que devuelve 3 trivias sobre el número ingresado."""
    return trivia_fetch(num)

def main():
    print("Hello learners!")

if __name__ == "__main__":
    main()
