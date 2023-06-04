import f_manipulacao as fm
import f_print as fp
import f_input as fi

fp.boas_vindas()
fp.menu_principal()
escolha = fi.opcao_menu_principal()

while escolha != 0:

    if escolha == 1:
        escolha_compras = fi.opcao_menu_compras()
        if escolha_compras == 1:
            fm.nova_compra()
        elif escolha_compras == 2:
            # aqui
            pass

    elif escolha == 2:
        # menu produtos
        pass

    elif escolha == 3:
        # menu clientes
        pass

    elif escolha == 4:
        # menu vendedores
        pass

    elif escolha == 5:
        # menu relatórios
        pass

    else:
        fp.mensagem_erro()
    
    escolha = fi.opcao_menu_principal()