from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para el login
class UserLogin(BaseModel):
    username: str
    password: str


class ProductInput(BaseModel):
    title: str
    price: float
    description: str
    category: str
    image: str

# --- NUEVA BASE DE DATOS DE PRODUCTOS (Aventura y Supervivencia) ---
products_db = [
  {
    "id": 1,
    "title": "Mochila Táctica Militar de Expedición 50L",
    "price": 125.50,
    "description": "Mochila robusta y resistente al agua, diseñada para senderismo extremo y campamentos de varios días. Múltiples compartimentos y soporte lumbar ergonómico.",
    "category": "equipo de campamento",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
    "rating": {"rate": 4.8, "count": 140}
  },
  {
    "id": 2,
    "title": "Camisa Térmica de Manga Larga Antihumedad",
    "price": 28.99,
    "description": "Prenda ligera y transpirable con tecnología de secado rápido. Ideal para mantener la temperatura corporal estable durante caminatas largas.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
    "rating": {"rate": 4.5, "count": 310}
  },
  {
    "id": 3,
    "title": "Chaqueta Impermeable Acolchada para Montaña",
    "price": 89.00,
    "description": "Chaqueta cortavientos e impermeable para climas fríos y lluviosos. Forro interno térmico desmontable para máxima versatilidad.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
    "rating": {"rate": 4.9, "count": 520}
  },
  {
    "id": 4,
    "title": "Pantalón Cargo Ajustable de Trekking",
    "price": 24.50,
    "description": "Pantalón flexible y duradero con bolsillos laterales reforzados. Tela resistente a desgarros para terrenos difíciles.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_t.png",
    "rating": {"rate": 4.2, "count": 190}
  },
  {
    "id": 5,
    "title": "Brújula de Supervivencia de Latón con Espejo Solar",
    "price": 45.00,
    "description": "Instrumento de navegación clásico de alta precisión, relleno de líquido para una lectura rápida y carcasa metálica ultrarresistente.",
    "category": "accesorios de supervivencia",
    "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_t.png",
    "rating": {"rate": 4.7, "count": 95}
  },
  {
    "id": 6,
    "title": "Anillo de Titanio Multiusos para Emergencias",
    "price": 35.00,
    "description": "Anillo minimalista de grado aeroespacial con micro-herramientas de corte integradas y alta resistencia a impactos.",
    "category": "accesorios de supervivencia",
    "image": "https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_t.png",
    "rating": {"rate": 4.0, "count": 65}
  },
  {
    "id": 7,
    "title": "Silbato de Emergencia de Alta Frecuencia",
    "price": 12.99,
    "description": "Silbato de rescate de doble tubo capaz de emitir hasta 120 decibelios para señales de auxilio a grandes distancias.",
    "category": "accesorios de supervivencia",
    "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_t.png",
    "rating": {"rate": 4.3, "count": 215}
  },
  {
    "id": 8,
    "title": "Kit de Anzuelos y Sedal de Pesca de Bolsillo",
    "price": 15.00,
    "description": "Mini estuche hermético con aparejos de pesca esenciales para situaciones de supervivencia en la naturaleza.",
    "category": "accesorios de supervivencia",
    "image": "https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_t.png",
    "rating": {"rate": 4.1, "count": 110}
  },
  {
    "id": 9,
    "title": "Disco Duro Externo Antigolpes 2TB USB 3.1",
    "price": 79.99,
    "description": "Unidad de almacenamiento portátil con cubierta de goma resistente a caídas y protección contra salpicaduras de agua.",
    "category": "tecnología y energía",
    "image": "https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_t.png",
    "rating": {"rate": 4.4, "count": 280}
  },
  {
    "id": 10,
    "title": "SSD Interno de Alto Rendimiento 1TB SATA III",
    "price": 95.00,
    "description": "Optimiza la velocidad de carga de tus mapas offline, software de navegación y sistemas multimedia portátiles.",
    "category": "tecnología y energía",
    "image": "https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_t.png",
    "rating": {"rate": 4.6, "count": 410}
  },
  {
    "id": 11,
    "title": "Tarjeta MicroSD de Alta Resistencia 256GB con Adaptador",
    "price": 39.99,
    "description": "Diseñada para cámaras de acción y drones; soporta temperaturas extremas, rayos X y caídas de agua.",
    "category": "tecnología y energía",
    "image": "https://fakestoreapi.com/img/71kWymZ+c+L._AC_SX679_t.png",
    "rating": {"rate": 4.9, "count": 350}
  },
  {
    "id": 12,
    "title": "Batería Externa Solar de Gran Capacidad 20,000 mAh",
    "price": 49.99,
    "description": "Cargador portátil con panel solar integrado y linterna LED de emergencia, perfecto para largas travesías sin conexión eléctrica.",
    "category": "tecnología y energía",
    "image": "https://fakestoreapi.com/img/61mtL65D4cL._AC_SX679_t.png",
    "rating": {"rate": 4.7, "count": 480}
  },
  {
    "id": 13,
    "title": "Panel Solar Portátil Plegable 60W para Campamento",
    "price": 149.99,
    "description": "Cargador solar de alta conversión con puertos USB múltiples para alimentar dispositivos móviles y baterías de campo.",
    "category": "tecnología y energía",
    "image": "https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_t.png",
    "rating": {"rate": 4.5, "count": 180}
  },
  {
    "id": 14,
    "title": "Estación de Energía Portátil de 500W con Salida AC",
    "price": 450.00,
    "description": "Generador de energía silencioso para campamentos base, capaz de mantener refrigeradores pequeños, luces y equipos de comunicación.",
    "category": "tecnología y energía",
    "image": "https://fakestoreapi.com/img/81Zt42ioCgL._AC_SX679_t.png",
    "rating": {"rate": 4.8, "count": 125}
  },
  {
    "id": 15,
    "title": "Chaqueta Polar Montañera 3 en 1 para Clima Extremo",
    "price": 75.00,
    "description": "Sistema de doble capa con polar interno extraíble y capa exterior cortavientos. Máximo aislamiento térmico.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_t.png",
    "rating": {"rate": 4.6, "count": 240}
  },
  {
    "id": 16,
    "title": "Chaqueta Rompevientos Estilo Motociclista de Lona Reforzada",
    "price": 65.00,
    "description": "Diseño resistente a la abrasión con protecciones ligeras en codos y hombros para rodadas en carretera y campo traviesa.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_t.png",
    "rating": {"rate": 4.3, "count": 305}
  },
  {
    "id": 17,
    "title": "Poncho Impermeable Largo con Capucha para Lluvia Torrencial",
    "price": 22.50,
    "description": "Capa impermeable ultraligera de cobertura total, adaptable para llevar con mochila grande incluida debajo.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2t.png",
    "rating": {"rate": 4.4, "count": 512}
  },
  {
    "id": 18,
    "title": "Playera Deportiva de Secado Rápido con Protección UV",
    "price": 18.00,
    "description": "Tejido técnico con factor de protección solar UPF 50+, ideal para exposición prolongada al sol bajo el aire libre.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/71z3kpMAYsL._AC_UY879_t.png",
    "rating": {"rate": 4.7, "count": 175}
  },
  {
    "id": 19,
    "title": "Camiseta de Compresión Térmica sin Costuras",
    "price": 16.50,
    "description": "Diseñada para mejorar la circulación sanguínea y evitar rozaduras durante actividades físicas intensas.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_t.png",
    "rating": {"rate": 4.5, "count": 198}
  },
  {
    "id": 20,
    "title": "Playera de Algodón Orgánico para Campamento Casual",
    "price": 14.99,
    "description": "Comodidad absoluta para momentos de descanso alrededor de la fogata al finalizar el día.",
    "category": "ropa outdoor",
    "image": "https://fakestoreapi.com/img/61pHAEJ4NML._AC_UX679_t.png",
    "rating": {"rate": 4.2, "count": 160}
  }
]

# --- NUEVA BASE DE DATOS DE USUARIOS ---
users_db = [
  {
    "address": {"geolocation": {"lat": "19.4326", "long": "-99.1332"}, "city": "mexico city", "street": "reforma", "number": 104, "zipcode": "06000"},
    "id": 1,
    "email": "carlos.aventura@gmail.com",
    "username": "carlos_exp",
    "password": "SecurePass#1",
    "name": {"firstname": "carlos", "lastname": "mendoza"},
    "phone": "55-1234-5678"
  },
  {
    "address": {"geolocation": {"lat": "20.5888", "long": "-100.3899"}, "city": "queretaro", "street": "circunvalacion", "number": 42, "zipcode": "76000"},
    "id": 2,
    "email": "sofia.trek@gmail.com",
    "username": "sofia_trek",
    "password": "Trek2026!",
    "name": {"firstname": "sofia", "lastname": "gomez"},
    "phone": "442-987-6543"
  },
  {
    "address": {"geolocation": {"lat": "25.6866", "long": "-100.3161"}, "city": "monterrey", "street": "hidalgo", "number": 510, "zipcode": "64000"},
    "id": 3,
    "email": "luis.sobrevive@gmail.com",
    "username": "luis_surv",
    "password": "SurvPass#99",
    "name": {"firstname": "luis", "lastname": "garza"},
    "phone": "81-5555-4321"
  },
  {
    "address": {"geolocation": {"lat": "20.6597", "long": "-103.3496"}, "city": "guadalajara", "street": "chapultepec", "number": 230, "zipcode": "44100"},
    "id": 4,
    "email": "ana.montana@gmail.com",
    "username": "ana_hikes",
    "password": "MountainKey4",
    "name": {"firstname": "ana", "lastname": "torres"},
    "phone": "33-4433-2211"
  },
  {
    "address": {"geolocation": {"lat": "21.1619", "long": "-86.8515"}, "city": "cancun", "street": "kukulcan", "number": 15, "zipcode": "77500"},
    "id": 5,
    "email": "diego.camp@gmail.com",
    "username": "diego_camp",
    "password": "BeachCamp#7",
    "name": {"firstname": "diego", "lastname": "rodriguez"},
    "phone": "998-111-2233"
  }
]

# --- NUEVA BASE DE DATOS DE CARRITOS ---
carts_db = [
  {
    "id": 1,
    "userId": 1,
    "date": "2026-10-01T10:00:00.000Z",
    "products": [{"productId": 1, "quantity": 2}, {"productId": 5, "quantity": 1}, {"productId": 12, "quantity": 1}]
  },
  {
    "id": 2,
    "userId": 2,
    "date": "2026-10-05T14:30:00.000Z",
    "products": [{"productId": 3, "quantity": 1}, {"productId": 2, "quantity": 3}]
  },
  {
    "id": 3,
    "userId": 3,
    "date": "2026-10-08T09:15:00.000Z",
    "products": [{"productId": 9, "quantity": 1}, {"productId": 13, "quantity": 1}]
  }
]


# --- RUTAS / ENDPOINTS DE PRODUCTOS ---
@app.get("/products/categories")
def get_categories():
    return sorted({p["category"] for p in products_db})

@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    filtered = [p for p in products_db if p["category"].lower() == category_name.lower()]
    return filtered

@app.get("/products")
def get_products():
    return products_db

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for p in products_db:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", status_code=201)
def create_product(product: ProductInput):
    product_data = product.dict()
    product_data.update({
        "id": max((p["id"] for p in products_db), default=0) + 1,
        "rating": {"rate": 0, "count": 0},
    })
    products_db.append(product_data)
    return product_data

@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductInput):
    for existing_product in products_db:
        if existing_product["id"] == product_id:
            existing_product.update(product.dict())
            return existing_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products_db):
        if product["id"] == product_id:
            return products_db.pop(index)
    raise HTTPException(status_code=404, detail="Product not found")


# --- RUTAS / ENDPOINTS DE USUARIOS ---
@app.get("/users")
def get_users():
    return users_db

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in users_db:
        if u["id"] == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")


# --- RUTAS / ENDPOINTS DE CARRITOS ---
@app.get("/carts")
def get_carts():
    return carts_db

@app.get("/carts/{cart_id}")
def get_cart(cart_id: int):
    for c in carts_db:
        if c["id"] == cart_id:
            return c
    raise HTTPException(status_code=404, detail="Cart not found")


# --- ENDPOINT DE AUTENTICACIÓN ---
@app.post("/auth/login")
def login(user: UserLogin):
    for u in users_db:
        if u["username"] == user.username and u["password"] == user.password:
            return {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.adventure-store-jwt-token"}
    raise HTTPException(status_code=401, detail="Authentication failed")
  