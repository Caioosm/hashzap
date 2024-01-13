#titulo hashzap
# botao de iniciar o chat
#     Popup
#         bem vindo ao hashzap
#         escreva seu nome
#         entrar no chat
# chat
#     usuario entrou no chat
#     mensagens do usuario
# campo para enviar mensagem
# botao de enviar

import flet as ft

def main(pagina):
    texto = ft.Text("HashZap")

    nome_usuario = ft.TextField(label='Escreva seu nome')
    chat = ft.Column()
    
    def msg_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(msg_tunel)

    def enviar_msg(evento):
        #colocar o nome do usuario na mensagem
        texto_campo_msg = f"{nome_usuario.value}: {campo_msg.value}"
        pagina.pubsub.send_all(texto_campo_msg)
        #limpar o campo mensagem
        campo_msg.value = ""
        pagina.update()

    campo_msg = ft.TextField(label='Digite uma mensagem', on_submit=enviar_msg)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_msg)
    
    def entrar_chat(evento):
        #feche o popup
        popup.open = False
        #tire o botao iniciar chat da tela
        pagina.remove(bt_iniciar)
        #adicionar o chat
        pagina.add(chat)
        #criar campo de envio de mensagem
        linha_msg = ft.Row(
            [
            campo_msg, 
            botao_enviar
            ]
        )
        pagina.add(linha_msg)
        #criar botao de enviar mensagem
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()



    def cancelar(evento):
        popup.open = False
        pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text('Bem vindo ao HashZap!'),
        content= nome_usuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrar_chat), ft.ElevatedButton('Cancelar', on_click=cancelar)]
        )
    

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    bt_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    
    pagina.add(texto)
    pagina.add(bt_iniciar)

# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)