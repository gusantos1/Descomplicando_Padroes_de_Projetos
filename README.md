# Descomplicando Padrões de Projeto com Python

Leitura e entendimento de baixa complexidade para compreensão dos principais padrões de projetos que podemos implementar com o Python.

Desconsideraremos o uso de Interfaces, Protocols, Type hints e encapsulamentos que não afetará na implementação e consequentemente manteremos a baixa complexidade com um nível de leitura de código mais acessível.  



### 1. Observer

<img src="C:\Users\GuilhermeSilvadosSan\Documents\github\Padroes-de-projetos\imgs\observer.svg">

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

<img src="C:\Users\GuilhermeSilvadosSan\Documents\github\Padroes-de-projetos\imgs\observer-final.svg">

#### Observer no mundo real

1. Assinaturas de newsletters: A cada atualização todos os assinantes recebem o conteúdo.
2. Após uma compra, você pode aguardar em casa e o seu porteiro te notificará quando chegar.



Leitura técnica completa: https://refactoring.guru/pt-br/design-patterns/observer