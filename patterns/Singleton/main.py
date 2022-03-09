from source import BRIDGE


bridge_one = BRIDGE
bridge_two = BRIDGE

bridge_one.adicionar_filial('SP')
bridge_two.adicionar_filial('BA')

BRIDGE.mostrar_filiais()

print(bridge_one == bridge_two == BRIDGE)
print(id(bridge_one))
print(id(bridge_two))
print(id(BRIDGE))