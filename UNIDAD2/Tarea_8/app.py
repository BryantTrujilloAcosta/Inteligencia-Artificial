import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.corpus import stopwords

# Descargar stopwords si no están disponibles
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class SpamClassifierApp:
    def __init__(self, master):
        """
        Inicializa la aplicación y configura la interfaz gráfica.
        """
        self.master = master
        master.title("Clasificador de Correos Spam")
        master.geometry("800x600")
        self.color_fondo = "#2F4F7F"
        master.configure(bg=self.color_fondo, padx=50, pady=50)
        
        # Inicializar variables
        self.modelo_listo = False
        
        # Preparar el modelo
        self.preparar_modelo()
        
        # Construir la interfaz
        self.crear_interfaz()
    
    def preparar_modelo(self):
        """
        Carga el dataset, realiza preprocesamiento y entrena el modelo Naïve Bayes.
        """
        try:
            # Verificar que el archivo existe
            dataset_path = "dataset/spam_assassin.csv"
            if not os.path.exists(dataset_path):
                print(f"Error: No se encontró el archivo {dataset_path}")
                messagebox.showerror("Error", f"No se encontró el archivo {dataset_path}. Verifique que el archivo existe en el directorio correcto.")
                return
            
            # Cargar el dataset
            print(f"Intentando cargar dataset desde {dataset_path}...")
            correos = pd.read_csv(dataset_path)
            print(f"Dataset cargado: {len(correos)} filas")
            
            # Verificar que las columnas necesarias existen
            if 'text' not in correos.columns or 'target' not in correos.columns:
                print("Error: El dataset no tiene las columnas requeridas 'text' y 'target'")
                messagebox.showerror("Error", "El dataset no tiene el formato correcto. Se requieren las columnas 'text' y 'target'.")
                return
            
            # Preprocesamiento
            print("Aplicando preprocesamiento...")
            correos = correos.drop_duplicates(subset="text").copy()
            correos['text'] = correos['text'].str.lower()
            
            # Obtener stopwords en español e inglés
            palabras_vacias = set(stopwords.words('spanish')).union(set(stopwords.words('english')))
            
            # Eliminar palabras vacías
            correos['text'] = correos['text'].apply(lambda x: ' '.join(
                palabra for palabra in x.split() if palabra not in palabras_vacias))
            
            # Filtrar correos vacíos
            correos = correos[correos['text'].str.strip() != '']
            
            # Verificar si quedaron suficientes datos
            if len(correos) < 10:
                print("Error: Después del preprocesamiento quedan muy pocos datos")
                messagebox.showerror("Error", "Después del preprocesamiento quedan muy pocos datos para entrenar el modelo.")
                return
            
            print(f"Preprocesamiento completado: {len(correos)} filas válidas")
            
            # Preparar para modelo
            self.vectorizador = CountVectorizer()
            
            # Dividir datos
            self.entrenamiento_x, self.prueba_x, self.entrenamiento_y, self.prueba_y = train_test_split(
                correos['text'],
                correos['target'],
                test_size=0.25,
                random_state=42
            )
            
            print(f"Datos divididos: {len(self.entrenamiento_x)} para entrenamiento, {len(self.prueba_x)} para prueba")
            
            # Entrenar modelo
            print("Entrenando modelo...")
            matriz_entrenamiento_x = self.vectorizador.fit_transform(self.entrenamiento_x)
            self.modelo_bayes = MultinomialNB()
            self.modelo_bayes.fit(matriz_entrenamiento_x, self.entrenamiento_y)
            
            # Evaluar modelo
            matriz_prueba_x = self.vectorizador.transform(self.prueba_x)
            self.precision = self.modelo_bayes.score(matriz_prueba_x, self.prueba_y)
            print(f"Precisión del modelo: {self.precision:.4f}")
            
            self.modelo_listo = True
            messagebox.showinfo("Éxito", f"Modelo entrenado correctamente con precisión de {self.precision:.4f}")
            
        except Exception as e:
            import traceback
            print(f"Error al preparar el modelo: {e}")
            print(traceback.format_exc())
            messagebox.showerror("Error", f"Error al preparar el modelo: {e}\nRevise la consola para más detalles.")
    
    def crear_interfaz(self):
        """
        Construye la interfaz gráfica de la aplicación.
        """
        # Título
        tk.Label(
            self.master, 
            text="Clasificador de Correos Spam", 
            font=("Courier", 20, "bold"), 
            bg=self.color_fondo,
            fg="white"
        ).grid(row=0, column=0, columnspan=2, pady=20)
        
        # Asunto
        tk.Label(
            self.master, 
            text="Asunto:", 
            font=("Courier", 14),
            bg=self.color_fondo,
            fg="white"
        ).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        
        self.asunto_entry = tk.Entry(self.master, font=("Courier", 14), width=40)
        self.asunto_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        
        # Mensaje
        tk.Label(
            self.master,
            text="Mensaje:",
            font=("Courier", 14),
            bg=self.color_fondo,
            fg="white"
        ).grid(row=2, column=0, sticky="ne", padx=10, pady=10)
        
        self.mensaje_text = scrolledtext.ScrolledText(
            self.master, 
            font=("Courier", 14), 
            height=10,
            width=60
        )
        self.mensaje_text.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        
        # Botones
        self.frame_botones = tk.Frame(self.master, bg=self.color_fondo)
        self.frame_botones.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.clasificar_btn = tk.Button(
            self.frame_botones,
            text="Clasificar",
            font=("Courier", 14),
            command=self.clasificar_correo,
            bg="white",
            fg="black",
            padx=10,
            pady=5
        )
        self.clasificar_btn.pack(side=tk.LEFT, padx=10)
        
        self.limpiar_btn = tk.Button(
            self.frame_botones, 
            text="Limpiar",
            font=("Courier", 14),
            command=self.limpiar_campos,
            bg="white",
            fg="black",
            padx=30,
            pady=5,
        )
        self.limpiar_btn.pack(side=tk.LEFT, padx=10)
        
        # Información del modelo
        if self.modelo_listo:
            estado_modelo = f"Modelo listo - Precisión: {self.precision:.4f}"
            color_texto = "green"
        else:
            estado_modelo = "Modelo no cargado"
            color_texto = "red"
            
        self.estado_modelo_label = tk.Label(
            self.master,
            text=estado_modelo,
            font=("Courier", 12),
            bg=self.color_fondo,
            fg=color_texto
        )
        self.estado_modelo_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Resultados
        self.frame_resultado = tk.Frame(self.master, bg="#E0E0E0", padx=20, pady=20)
        self.frame_resultado.grid(row=5, column=0, columnspan=2, sticky="ew", padx=20, pady=20)
        
        tk.Label(
            self.frame_resultado, 
            text="Resultado:", 
            font=("Courier", 14, "bold"),
            bg="#E0E0E0",
            fg="black"
        ).grid(row=0, column=0, sticky="w")
        
        self.resultado_label = tk.Label(
            self.frame_resultado, 
            text="Esperando análisis...", 
            font=("Courier", 14),
            bg="#E0E0E0",
            fg="black"
        )
        self.resultado_label.grid(row=0, column=1, sticky="w", padx=10)
        
        tk.Label(
            self.frame_resultado,
            text="Probabilidad:",
            font=("Courier", 14, "bold"),
            bg="#E0E0E0",
            fg="black"
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        self.probabilidad_label = tk.Label(
            self.frame_resultado, 
            text="--", 
            font=("Courier", 14),
            bg="#E0E0E0"
        )
        self.probabilidad_label.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        
        # Configuraciones del grid
        self.master.grid_columnconfigure(1, weight=1)
    
    def clasificar_correo(self):
        """
        Clasifica el correo ingresado por el usuario como SPAM o NO SPAM.
        """
        if not self.modelo_listo:
            messagebox.showerror("Error", "El modelo no está listo para clasificar. Verifique que el dataset se cargó correctamente.")
            return
        
        asunto = self.asunto_entry.get().strip()
        mensaje = self.mensaje_text.get("1.0", tk.END).strip()
        
        if not mensaje and not asunto:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un asunto o mensaje para clasificar")
            return
        
        # Combinar asunto y mensaje para clasificar
        texto_completo = f"{asunto} {mensaje}"
        
        # Preprocesamiento básico
        texto_completo = texto_completo.lower()
        
        # Vectorizar
        try:
            texto_vectorizado = self.vectorizador.transform([texto_completo])
            
            # Predecir
            prediccion = self.modelo_bayes.predict(texto_vectorizado)
            prob_spam = self.modelo_bayes.predict_proba(texto_vectorizado)[0, 1]
            
            # Mostrar resultado
            if prediccion[0] == 1:
                self.resultado_label.config(text="SPAM", fg="red")
            else:
                self.resultado_label.config(text="NO SPAM", fg="green")
            
            self.probabilidad_label.config(text=f"{prob_spam:.2%} de ser spam")
            
            # Cambiar color de fondo según resultado
            if prediccion[0] == 1:
                self.frame_resultado.config(bg="#FFCDD2")  # Rojo claro para spam
                self.resultado_label.config(bg="#FFCDD2")
                self.probabilidad_label.config(bg="#FFCDD2")
            else:
                self.frame_resultado.config(bg="#C8E6C9")  # Verde claro para no spam
                self.resultado_label.config(bg="#C8E6C9")
                self.probabilidad_label.config(bg="#C8E6C9")
                
        except Exception as e:
            print(f"Error al clasificar el correo: {e}")
            messagebox.showerror("Error", f"Error al clasificar el correo: {e}")
    
    def limpiar_campos(self):
        self.asunto_entry.delete(0, tk.END)
        self.mensaje_text.delete("1.0", tk.END)
        self.resultado_label.config(text="Esperando análisis...", fg="black")
        self.probabilidad_label.config(text="--")
        self.frame_resultado.config(bg="#E0E0E0")
        self.resultado_label.config(bg="#E0E0E0")
        self.probabilidad_label.config(bg="#E0E0E0")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = SpamClassifierApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Error en la aplicación: {e}")
        messagebox.showerror("Error crítico", f"Error al iniciar la aplicación: {e}")