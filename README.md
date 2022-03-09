# Descomplicando Padrões de Projeto com Python

Leitura e entendimento de baixa complexidade para compreensão dos principais padrões de projetos que podemos implementar com o Python.

Desconsideraremos o uso de Interfaces, Protocols, Type hints e encapsulamentos que não afetará na implementação e consequentemente manteremos a baixa complexidade com um nível de leitura de código mais acessível.  



### 1. Observer

<img src="https://raw.githubusercontent.com/gusantos1/Descomplicando_Padroes_de_Projetos/a90efd626b99c87aea4e561a9498f31825a21570/imgs/observer.svg">

O objetivo desse padrão é notificar um evento aos objetos que estão aguardando pela notificação. De modo prático, teremos um objeto que armazenará objetos de outra classe e através de um método, notificará os objetos que foram armazenados.

```python
class Observador:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
    def receber_notificacao(self, msg):
        print(f'{msg} para {self.nome}')

caio = Observador('Caio', 'caio22@gmail.com')
fernanda = Observador('Fernanda', 'fernanda33@gmail.com')
marcela = Observador('Marcela', 'marcela21@gmail.com')
observadores = [caio, fernanda, marcela]
```
1. Criamos simples objetos observadores com um método que receberá uma msg de notificação.


```python
class Observavel:
    def __init__(self):
        self.observadores = []
    
    def adicionar_observador(self, observador):
        self.observadores.append(observador)
   	
    def notificar(self, msg):
        for observador in self.observadores:
            observador.receber_notificacao(msg)

obs = Observavel()
```

2. Criamos um simples objeto observável que adicionará objetos do tipo observador e notificará esses objetos por um método de notificação. Conseguimos chamar o método **receber_notificacao** dentro da classe Observavel porque nossos objetos são do tipo Observador.

````python
for observador in observadores:
    obs.adicionar_observador(observador)
````

3. Adicionamos os observadores em self.observadores.

```python
obs.notificar('Desconto exclusivo de 20%')
```
4. Notificando os objetos observadores.

```shell
Output:

Desconto exclusivo de 20% para Caio
Desconto exclusivo de 20% para Fernanda
Desconto exclusivo de 20% para Marcela
```

#### ainda_não_entendi()

<img src="https://raw.githubusercontent.com/gusantos1/Descomplicando_Padroes_de_Projetos/a90efd626b99c87aea4e561a9498f31825a21570/imgs/observer-final.svg">

#### Observer no mundo real

1. Assinaturas de newsletters: A cada atualização todos os assinantes recebem o conteúdo.
2. Após uma compra, você pode aguardar em casa e o seu porteiro te notificará quando chegar.



Leitura técnica completa: https://refactoring.guru/pt-br/design-patterns/observer

### 2. Singleton

O objetivo desse padrão é manter uma única instância por classe. De modo prático, em python, uma maneira simples de implementar esse padrão é modularizar a pasta com o objeto já criado; isso preservará a existência de uma única instância.





```bash
────Singleton
    │   main.py
    └───source
            model.py
            pattern.py
            __init__.py
```

1. Árvore de diretório da estrutura da implementação.

```python
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.filiais = []
    
    def adicionar_filial(self, local):
        self.filiais.append(local)
    
    def mostrar_filiais(self):
        print(self.filiais)
```

2. Nossa classe Empresa em model.py com a finalidade de ter apenas uma única instância pra cada Empresa, com a possibilidade de adicionar e mostrar suas filiais.

```python
from source.model import Empresa


BRIDGE = Empresa('Bridge')
```

3. Em pattern.py temos a criação do nosso objeto BRIDGE como uma constante.

```python
from source.pattern import BRIDGE
```

4. No __ init __.py a ideia é fazer com que o objeto `BRIDGE` faça parte da importação toda vez que o `source` for chamado como módulo, da mesma forma quando usamos para importar funcionalidades em bibliotecas, como: `from math import radians`, 

```python
from source import BRIDGE


bridge_one = BRIDGE
bridge_two = BRIDGE

bridge_one.adicionar_filial('SP')
bridge_two.adicionar_filial('BA')
```

5. Criamos duas variáveis atribuindo o mesmo objeto BRIDGE e em cada variável chamados o método adicionar_filial.

```bash
BRIDGE.mostrar_filiais()
print(bridge_one == bridge_two == BRIDGE)

print(id(bridge_one))
print(id(bridge_two))
print(id(BRIDGE))

Output:
    ['SP', 'BA']
	True
	2296464390656
    2296464390656
    2296464390656
```

6. Vemos que em ambas variáveis o objeto BRIDGE é chamado e preservado como única instância e o mesmo id.