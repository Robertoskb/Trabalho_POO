txtFixo = "Assim que acabar de escutar a frase “O que você quer fazer hoje?” o programa" \
          " vai aguardar você utilizar algum dos comandos:"

aboutButton = " Sobre. Ao falar “sobre”... o programa irá te contar algumas curiosidades " \
              "sobre esse aplicativo e quem o desenvolveu."

helpButton = "Ajuda. Ao falar “ajuda”... o programa irá explicar a função " \
             "de cada comando desse aplicativo."

commandButton = " Comandos. Ao falar “comandos”... o programa irá listar " \
                "o nome de cada comando desse aplicativo."

add_reminderButton = " Adicionar Lembrete. Ao falar “adicionar lembrete”... o programa irá te perguntar" \
                     " “qual o conteúdo do lembrete” que você quer adicionar " \
                     "(exemplo: Fazer compras às 14 horas). Após isso, perguntará se " \
                     "“seu lembrete tem período de duração”, ou seja, se tem data para expirar: " \
                     "você terá duas opções. “Sim” e “Não”. Caso responda que “Sim” pedirá " \
                     "para que você informe o número de dias que seu lembrete ficará disponível " \
                     "(o número de dias estará limitado de 1 a 30 dias). Se você quiser " \
                     "que fique somente 1 dia no programa, diga: “um dia”. Caso responda que “Não”" \
                     " o programa te informará que o lembrete ficará disponível durante 2 dias." \
                     "Ao final do processo de adição de um novo lembrete " \
                     "será avisado “lembrete salvo com sucesso!”."

list_reminderButton = " Listar Lembretes. Ao falar “listar lembretes”... o programa dirá " \
                      "quantos lembretes ainda estão disponíveis no aplicativo. Após isso, " \
                      "o programa vai listar cada lembrete por ordem de prioridade" \
                      " (primeiro os que estão mais perto de expirar e por último os " \
                      "que têm o período de duração maior), informará o número em que " \
                      "esse lembrete se encontra na lista, vai descrever o conteúdo do respectivo" \
                      " lembrete e avisar em quanto tempo expirará" \
                      " (exemplo: Lembrete 1. Comprar Shampoo. 4 dias restantes)." \
                      "Quando a listagem de todos os lembretes adicionados terminar, " \
                      "será avisado “fim da lista de lembretes”."

delete_reminderButton = " Excluir Lembrete. Ao falar “excluir”... o programa irá recomendar " \
                        "a utilização do comando “Listar Lembretes” para que possa ter a certeza" \
                        " do conteúdo e número do lembrete que você deseja excluir. " \
                        "Logo após isso, o programa pedirá o número do lembrete que você deseja excluir." \
                        "Depois que você informar o número do lembrete, o programa " \
                        "pedirá uma confirmação lendo o conteúdo do lembrete " \
                        "(você terá duas opções de resposta: “Sim” ou “Não”.)" \
                        "Caso responda que “Sim”, o programa informará “lembrete excluído com sucesso!“" \
                        "Caso responda que “Não”, o programa retornará para a pergunta " \
                        "“O que você quer fazer hoje?”."

exitButton = " Sair. Ao falar “sair”... o programa irá se despedir de você e fechará o aplicativo."

all_helps = txtFixo + aboutButton + helpButton + commandButton + add_reminderButton + list_reminderButton + delete_reminderButton
