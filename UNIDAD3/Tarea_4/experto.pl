% ------------------------
% PREGUNTAS
% ------------------------
pregunta(p1,  '¿Te gusta trabajar con matemáticas?').
pregunta(p2,  '¿Te gusta resolver problemas numéricos complejos?').
pregunta(p3,  '¿Tienes interés en la programación?').
pregunta(p4,  '¿Tienes interés en el desarrollo de software?').
pregunta(p5,  '¿Te interesa la física, especialmente en temas como mecánica?').
pregunta(p6,  '¿Te interesa la física, especialmente en temas como electricidad?').
pregunta(p7,  '¿Disfrutas trabajar con circuitos?').
pregunta(p8,  '¿Te interesa trabajar con componentes electrónicos?').
pregunta(p9,  '¿Te interesa trabajar con sistemas eléctricos?').
pregunta(p10, '¿Te gusta diseñar o construir máquinas?').
pregunta(p11, '¿Te gusta construir mecanismos físicos?').
pregunta(p12, '¿Te interesa la integración de sistemas mecánicos?').
pregunta(p13, '¿Te interesa la integración de sistemas electrónicos?').
pregunta(p14, '¿Te interesa la integración de sistemas computacionales?').
pregunta(p15, '¿Te interesa la robótica?').
pregunta(p16, '¿Te interesa la química?').
pregunta(p17, '¿Te interesan los procesos biológicos?').
pregunta(p18, '¿Te interesa la biología?').
pregunta(p19, '¿Te interesa el estudio de sistemas vivos?').
pregunta(p20, '¿Disfrutas realizar experimentos en laboratorios?').
pregunta(p21, '¿Te preocupa el medio ambiente?').
pregunta(p22, '¿Te interesa trabajar en su conservación?').
pregunta(p23, '¿Tienes interés en la agricultura?').
pregunta(p24, '¿Tienes interés en soluciones sustentables para la producción de alimentos?').
pregunta(p25, '¿Prefieres trabajar al aire libre?').
pregunta(p26, '¿Prefieres trabajar en entornos de campo?').
pregunta(p27, '¿Te gustaría trabajar en el desarrollo de tecnologías para la comunicación?').
pregunta(p28, '¿Te atrae diseñar soluciones tecnológicas para mejorar la eficiencia de sistemas?').
pregunta(p29, '¿Te atrae implementar soluciones tecnológicas para mejorar la eficiencia de sistemas?').
pregunta(p30, '¿Prefieres trabajar en la optimización de procesos?').
pregunta(p31, '¿Prefieres trabajar en la gestión de recursos?').
pregunta(p32, '¿Tienes habilidades en el análisis de datos?').
pregunta(p33, '¿Tienes interés en el análisis de estadísticas?').
pregunta(p34, '¿Te sientes cómodo trabajando en una oficina?').
pregunta(p35, '¿Te sientes cómodo analizando datos?').
pregunta(p36, '¿Te sientes cómodo gestionando proyectos?').
pregunta(p37, '¿Disfrutas liderar equipos?').
pregunta(p38, '¿Disfrutas tomar decisiones estratégicas?').

:- dynamic respuesta/2.

inicio :-
    retractall(respuesta(_, _)),
    hacer_preguntas,
    mejor_carrera.

hacer_preguntas :-
    forall(pregunta(Cod, Preg), repetir_hasta_valido(Cod, Preg)).

repetir_hasta_valido(Cod, Preg) :-
    repeat,
    format('~w (si/no): ', [Preg]),
    read(Resp),
    (   (Resp == si ; Resp == no) ->
        assertz(respuesta(Cod, Resp)),
        !
    ;   format('Por favor responde con "si." o "no."~n'),
        fail
    ).

% ------------------------
% DEFINICIÓN DE REGLAS COMO LISTAS
% ------------------------

regla("Ingeniería Bioquímica", [p1-no, p2-no, p3-no, p4-no, p8-si, p9-si, p10-si, p16-si, p17-si, p18-si, p19-si, p20-si]).
regla("Ingeniería Ambiental", [p21-no, p22-si, p23-si, p24-no, p25-si, p26-no, p9-no, p18-si, p20-si]).
regla("Ingeniería Eléctrica", [p1-si, p3-si, p4-no, p5-si, p6-si, p7-si, p9-si, p12-si, p14-no]).
regla("Ingeniería Electrónica", [p1-si, p3-si, p4-si, p6-no, p7-si, p8-si, p13-si, p14-si, p12-no]).
regla("Ingeniería en Energías Renovables", [p21-no, p4-si, p3-no, p5-si, p6-si, p9-si, p23-si, p12-si, p15-no]).
regla("Ingeniería en Gestión Empresarial", [p30-no, p31-si, p33-si, p34-si, p36-si, p38-si, p37-no, p3-no, p1-no]).
regla("Ingeniería Industrial", [p1-no, p30-si, p31-si, p33-si, p34-si, p35-si, p36-si, p3-no, p4-no]).
regla("Ingeniería Mecánica", [p1-si, p3-no, p4-no, p5-si, p10-si, p11-si, p12-si, p14-no, p15-si]).
regla("Ingeniería Mecatrónica", [p1-si, p3-no, p4-no, p5-no, p6-si, p12-si, p13-si, p14-si, p15-si]).
regla("Ingeniería en Sistemas Computacionales", [p1-si, p2-no, p3-si, p4-si, p15-si, p33-si, p34-no, p14-si, p6-no]).
regla("Ingeniería en Tecnologías de la Información y Comunicaciones", [p2-no, p3-si, p4-si, p27-si, p33-no, p34-si, p28-si, p14-si, p15-no]).
regla("Ingeniería en Innovación Agrícola Sustentable", [p21-no, p22-si, p23-si, p24-si, p25-si, p26-si, p18-si, p19-si, p9-no]).

% ------------------------
% COMPARADOR DE REGLAS
% ------------------------

contar_coincidencias([], _, 0).
contar_coincidencias([P-R|T], Resp, N) :-
    ( member(P-R, Resp) -> contar_coincidencias(T, Resp, N1), N is N1 + 1
    ; contar_coincidencias(T, Resp, N) ).

mejor_carrera :-
    findall(P-R, respuesta(P,R), ListaResp),
    (   todas_iguales(ListaResp, si) ->
        format('~n*** No es posible realizar una recomendación: Todas las respuestas fueron "sí", por lo que no hay una carrera específica que se adapte mejor a tus preferencias.~n')
    ;   todas_iguales(ListaResp, no) ->
        format('~n*** No es posible realizar una recomendación: Todas las respuestas fueron "no", lo que indica que ninguna carrera coincide con tus intereses.~n')
    ;   findall(Nombre-Score, (
            regla(Nombre, Condiciones),
            contar_coincidencias(Condiciones, ListaResp, Score)
        ), Resultados),
        (   Resultados == [] ->
            format('~n*** No es posible realizar una recomendación: Ninguna carrera tiene suficientes coincidencias con tus respuestas.~n')
        ;   sort(2, @>=, Resultados, Ordenados),
            Ordenados = [Mejor-Valor|_],  % Aquí nos aseguramos de que Ordenados siempre tenga al menos una opción válida
            (   Valor == 0 ->
                format('~n*** No es posible realizar una recomendación: Ninguna carrera coincide lo suficiente con tus respuestas.~n')
            ;   mensaje_recomendacion(Mejor, Mensaje),
                format('~n*** RECOMENDACIÓN: ~w ~n', [Mejor]),
                format('Razón: ~w~n', [Mensaje])
            )
        )
    ).

todas_iguales([], _).
todas_iguales([_-Resp|T], Resp) :- todas_iguales(T, Resp).


mensaje_recomendacion("Ingeniería Bioquímica", "Se recomienda esta carrera porque tienes interés en la química, la biología y los procesos biológicos. Además, disfrutas trabajar en laboratorios y experimentar con nuevos materiales.").
mensaje_recomendacion("Ingeniería Ambiental", "Esta carrera es ideal para ti porque te interesa la conservación del medio ambiente y los procesos ecológicos. Además, te gusta la biología y trabajar en proyectos de sostenibilidad.").
mensaje_recomendacion("Ingeniería Eléctrica", "Se recomienda esta carrera porque disfrutas trabajar con circuitos eléctricos y te interesan la física y los sistemas eléctricos.").
mensaje_recomendacion("Ingeniería Electrónica", "Te gusta trabajar con componentes electrónicos, circuitos y sistemas computacionales. Además, tienes interés en la integración de tecnologías.").
mensaje_recomendacion("Ingeniería en Energías Renovables", "Te preocupas por el medio ambiente y buscas desarrollar tecnologías sustentables para el aprovechamiento energético.").
mensaje_recomendacion("Ingeniería en Gestión Empresarial", "Tienes habilidades en la gestión de recursos y optimización de procesos, además de interés en la toma de decisiones estratégicas.").
mensaje_recomendacion("Ingeniería Industrial", "Te interesa la optimización de procesos y la gestión eficiente de recursos").
mensaje_recomendacion("Ingeniería Mecánica", "Te apasiona diseñar y construir máquinas y mecanismos físicos, además de trabajar con sistemas mecánicos.").
mensaje_recomendacion("Ingeniería Mecatrónica", "Te interesan la robótica y la integración de sistemas mecánicos y electrónicos, además de aplicar conocimientos de física y programación.").
mensaje_recomendacion("Ingeniería en Sistemas Computacionales", "Tienes habilidades en programación y te interesa el desarrollo de software y el análisis de datos.").
mensaje_recomendacion("Ingeniería en Tecnologías de la Información y Comunicaciones", "Te atrae el diseño e implementación de soluciones tecnológicas para mejorar la eficiencia de los sistemas.").
mensaje_recomendacion("Ingeniería en Innovación Agrícola Sustentable", "Te interesa la agricultura y el desarrollo de soluciones sustentables para la producción de alimentos.").



