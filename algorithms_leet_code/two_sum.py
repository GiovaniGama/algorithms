def twoSum(nums, target: int):
    numDict = {} #criando um dicionario vazio
    for i, num in enumerate(nums): #passando por cada valor do array num
        complement = target - num
        if complement in numDict:
            return [numDict[complement], i]
        numDict[num] = i
        
arr = [1,4,5,6]
print(twoSum(arr, 5))

"""
def two_sum(nums, target):
Esta linha define uma função chamada two_sum que recebe dois parâmetros: nums, que é a lista de números, e target, que é o valor alvo que estamos tentando encontrar como a soma de dois números na lista.
num_dict = {}
Esta linha cria um dicionário vazio chamado num_dict. Este dicionário será usado para armazenar os números que já percorremos na lista nums.

for i, num in enumerate(nums):
Esta linha começa um loop que percorre os elementos da lista nums. A função enumerate retorna um objeto iterável que gera tuplas contendo o índice e o valor de cada elemento da lista.
complement = target - num
Aqui calculamos o complemento necessário para atingir o alvo (target - num). Por exemplo, se target for 9 e num for 2, o complemento será 7.

if complement in num_dict:
Esta linha verifica se o complemento calculado está presente no dicionário num_dict. Se estiver presente, isso significa que encontramos uma combinação válida de números cuja soma é igual ao alvo.
return [num_dict[complement], i]
Se encontrarmos uma combinação válida, retornamos uma lista contendo os índices desses dois números na lista nums. num_dict[complement] nos dá o índice do número cujo complemento foi encontrado, e i é o índice do número atual.

num_dict[num] = i
Se não encontrarmos uma combinação válida, adicionamos o número atual e seu índice ao dicionário num_dict. Isso nos permitirá verificar se o complemento necessário para o número atual já foi encontrado nos elementos anteriores da lista.
No exemplo de uso:

nums = [2, 7, 11, 15] é a lista de números fornecida.
target = 9 é o valor alvo que estamos tentando encontrar como a soma de dois números na lista.
print(two_sum(nums, target)) chama a função two_sum com os parâmetros nums e target e imprime o resultado retornado pela função. Neste caso, a saída esperada é [0, 1], indicando que os números nos índices 0 e 1 da lista nums (ou seja, 2 e 7) somam-se para igualar o alvo de 9.
"""