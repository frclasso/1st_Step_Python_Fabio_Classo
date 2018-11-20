Date and Time
=====================

Um programa em Python pode manipular data e hora de várias maneiras. E comum
realizarmos conversão entre formatos de data.

O que é Ticks?
--------------
A época do Unix (ou hora Unix ou hora POSIX ou carimbo de data / hora Unix) é o 
número de segundos que se passaram desde 1º de janeiro de 1970 
(meia-noite UTC / GMT), sem contar os segundos bissextos 
(em ISO 8601: 1970-01-01T00: 00 : 00Z). Literalmente, a época é o tempo 0 do 
Unix (meia-noite 1/1/1970), mas 'epoch' é frequentemente usado como sinônimo 
de Unixtime. Muitos sistemas Unix armazenam datas de época como um inteiro de 
32 bits assinado, o que pode causar problemas em 19 de janeiro de 2038 
(conhecido como o problema do ano 2038 ou Y2038).


Existe um módulo de tempo popular disponível em Python, que fornece funções
para trabalhar com tempos, e para converter entre representações. A função time.time
() retorna a hora atual do sistema em ticks desde as 00:00, 1 de janeiro de
1970(época).

Mais sobre:
-----------

https://en.wikipedia.org/wiki/Unix_time
https://en.wikipedia.org/wiki/Year_2038_problem


Conversores Datetime to Ticks:
------------------------------
https://www.epochconverter.com/




Exemplos:
- 01_datetime_to_ticks.py
- 02_local_time.py
- 03_current_time.py
- 04_formatted_time.py
- 05_obtendo_calendario_do_mes.py
- 06_altzone_method.py
- 07_asctime_method.py
- 08_timeclock_method.py
- 09_ctime_method.py
- 10_gmtime_method.py
- 11_localtime_method.py
- 12_mktime_method.py
- 13_sleep_method.py
- 14_strftime_method.py
- 15_strptime_method.py
- 16_time_method.py
- 17_tzset_method.py

* Na apostila teremos mais exemplos e outros metodos


Esse material foi desenvolvido por **Fabio R. Classo** para o curso de Linguagem de
Programação Python da **JCAVI** Treinamentos em T.I.


![Image](https://github.com/frclasso/apostila_python_modulo_1/blob/master/jcavi.png "JCAVI")

https://www.jcavitreinamentos.com.br/

https://www.facebook.com/jcavitreinamentos/

Contatos: frclasso@gmail.com

https://www.linkedin.com/in/fabio-reis-classo-46881425/


**[Pagina inicial](https://github.com/frclasso/apostila_python_modulo_1)**