from PyPDF2 import PdfReader, PdfWriter
import datetime

def modificar_metadatos_pdf(archivo_pdf, nuevos_metadatos):
    with open(archivo_pdf, 'rb') as archivo:
        pdf = PdfReader(archivo)
        
        # Crear un nuevo objeto PdfWriter
        nuevo_pdf = PdfWriter()
        
        # Copiar todas las páginas del PDF original al nuevo PDF
        for pagina_num in range(len(pdf.pages)):
            pagina = pdf.pages[pagina_num]
            nuevo_pdf.add_page(pagina)
        
        # Actualizar los metadatos
        nuevo_pdf.add_metadata(nuevos_metadatos)
        
        # Guardar el nuevo PDF con los metadatos modificados
        nuevo_nombre_pdf = f"nuevo_{archivo_pdf}"
        with open(nuevo_nombre_pdf, 'wb') as nuevo_archivo:
            nuevo_pdf.write(nuevo_archivo)
        
        print(f"Se ha creado el nuevo archivo PDF: {nuevo_nombre_pdf}")

# Ejemplo de uso
archivo_pdf = "pdf_name.pdf"

nuevos_metadatos = {
    '/Author': 'Autor del documento',
    '/Title': 'Título del documento',
    '/Subject': 'Asunto del documento (Descripción)',
    '/Keywords': 'Palabras, Clave',
    '/CreationDate': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
    '/ModDate': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
    '/Producer': 'OverlordAntony',
    # Agrega los metadatos adicionales que desees modificar
}

modificar_metadatos_pdf(archivo_pdf, nuevos_metadatos)
