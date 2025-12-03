from transformers import pipeline

print("Cargando modelo toxic-bert...")
print("La primera vez descargara el modelo, puede tardar unos minutos.\n")

# Cargar el modelo
classifier = pipeline("text-classification", 
                     model="unitary/toxic-bert",
                     top_k=None)

print("Modelo cargado correctamente!\n")

# Textos de prueba
test_texts = [
    "You are amazing and wonderful!",
    "I hate you, you are stupid!",
    "Machine learning is fascinating.",
    "This is the worst thing ever, I hope you fail!"
]

print("=" * 60)
print("PROBANDO EL MODELO")
print("=" * 60 + "\n")

for i, text in enumerate(test_texts, 1):
    print(f"Texto {i}: {text}")
    results = classifier(text)[0]
    
    # Mostrar resultados organizados
    print("Resultados:")
    for result in results:
        label = result['label']
        score = result['score']
        print(f"   {label:15s}: {score:.4f} ({score*100:.2f}%)")
    
    print("\n" + "-" * 60 + "\n")

print("Prueba completada exitosamente!")
