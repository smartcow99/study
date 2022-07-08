import flet
from flet import Page, TextField, Row, IconButton, icons

def main(page: Page):
  page.title = "Counter App"
  page.vertical_alignment = "center"
  
  txt_field = TextField(value="0", width=100, text_align="rigth")
  
  def minus_clicked(e) :
    txt_field.value = int(txt_field.value) - 1
    page.update()
  
  def plus_clicked(e) :
    txt_field.value = int(txt_field.value) + 1
    page.update()
  
  page.add(
    Row(
      [
        IconButton(icons.REMOVE, on_click=minus_clicked),
        txt_field,
        IconButton(icons.ADD, on_click=plus_clicked),
        
      ],
      alignment="center",
    )
  )
  
  flet.app(target=main, port=8080)