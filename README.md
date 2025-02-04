<h1>INTELIGENCIA ARTIFICIAL 9-10</h1>

## Tarea 1 Árbol Binario de Búsqueda

<h2>Integrantes de equipo</h2>
<ul>
<li>MENDOZA GARCIA BRAYAN</li>
<li>TRUJILLO ACOSTA BRYANT </li>
</ul>
<h2> Explicación </h2>
<p>En este proyecto se utiliza una clase llamada <strong>NodoArbol</strong> que es la que representa a un nodo en el árbol binario.</p> 
</p>Tiene 3 atributos los cuales son </p>
<ul>
<li>valor: Que representa el valor almacenado en el nodo.</li>
<li>izquierda: Referencia al hijo izquierdo el nodo con valor menor.</li>
<li>derecha: Referencia al hijo derecho el nodo con valor mayor.</li>
</ul>
<p>El constructor inicializa el nodo con valor y los hijos en none.</p>
<p><strong>Clase árbol</strong> representa al arbol binario.</p>
<p>Tiene un atributo <strong>raiz</strong> que es la referencia al nodo raíz del árbol.
tiene métodos para insertar valorers, buscar y recorrer el árbol </p>

<p>Métodos de la clase:</p>
<ul>
<li><strong>Insertar</strong> inserta un valor en el árbol si el árbol esta vacio, el valor se convierte en la raiz. si no se llama al metodo _insertar_recursivo para encontrar la posicion correcta.</li>
<li><strong>_inseetar_recursivo</strong> este metodo inserta un valor de manera recursiva compara el valor con el nodo actual y lo coloca a la izquierda si es menor o a la derecha si es mayor.No permite valores duplicados</li>
<li><strong>Buscar</strong> busca un valor en el árbol. Llama al método _buscar_recursivo para realizar la búsqueda.</li>
<li><strong>_buscar_recursivo</strong> busca un valor de manera recursiva Retorna True si el valor esta en el árboil y False si no.</li>
<li><strong>imprimir</strong>Recorre el árbol en order e imprime los valores. Llama al método _imprimir_recursivo.</li>
<li><strong>_imprimir_recursivo</strong> recorre el árbol en orden izquierda, raiz, derecha e imprime los valores</li>
</ul>

<h2>Uso</h2>
<ol>
<li>Se crea una instancia de Arbolbinario</li>
<li>Se inserta varios valors en el árbol como en este caso fue 10, 5, 15, 3, 7 </li>
<li>Se imprime el árbol en orden, se muestran los valores en orden de menor a mayor 3 5 7 10 15</li>
<li>Se busca el valor 7 (que está en el árbol) y se imprime True.</li>
<li>Se busca el valor 12 (que no está en el árbol) y se imprime False.</li>
</ol>

