# Create for David Robert, 06/06/2024 21:36

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import textract
import ftfy

# Definir habilidades técnicas por área
habilidades = {
    'Front-end': [
        'HTML', 'CSS', 'JavaScript',
        'React', 'Angular', 'Vue.js',
        'TypeScript', 'Bootstrap', 'jQuery'
    ],
    'Back-end': [
        'Python', 'Java', 'Node.js', 'PHP', 'Ruby',
        'Django', 'Flask', 'Spring Boot', 'Express.js', 'Laravel',
        'C#', '.NET', 'ASP.NET'
    ],
    'Banco de Dados': [
        'MySQL', 'PostgreSQL', 'MongoDB', 'Redis',
        'SQL Server', 'Oracle',
        'SQLite', 'Firebase'
    ],
    'Microservices/APIs': [
        'RESTful APIs', 'SOAP', 'Microservices',
        'GraphQL', 'Kafka', 'RabbitMQ'
    ],
    'Controle de Versão': [
        'Git', 'GitHub', 'GitLab',
        'SVN', 'Mercurial'
    ],
    'Metodologias Ágeis': [
        'Scrum', 'Kanban',
        'XP (Extreme Programming)', 'Lean'
    ],
    'DevOps': [
        'Jenkins', 'GitLab CI/CD', 'Docker',
        'Kubernetes', 'Ansible', 'Terraform'
    ],
    'CAD': [
        'AutoCAD', 'SolidWorks', 'CATIA', 'Fusion 360',
        'Blender', 'Maya', '3ds Max'
    ],
    'Machine Learning': [
        'TensorFlow', 'PyTorch', 'Keras',
        'Scikit-learn', 'Pandas', 'NumPy'
    ],
    'Data Science': [
        'R', 'MATLAB', 'SQL', 'Tableau',
        'Power BI', 'Apache Spark', 'Hadoop'
    ],
    'Cloud Computing': [
        'AWS', 'Azure', 'Google Cloud',
        'IBM Cloud', 'Heroku', 'DigitalOcean'
    ],
    'Sistemas Operacionais': [
        'Linux', 'Unix', 'Windows Server',
        'macOS', 'iOS', 'Android'
    ],
    'Redes e Segurança': [
        'TCP/IP', 'DNS', 'DHCP', 'Firewall',
        'VPN', 'SSL', 'Cryptography'
    ],
    'UX/UI Design': [
        'Adobe XD', 'Figma', 'Sketch',
        'InVision', 'Principle', 'UXPin'
    ],
    'Testing/QA': [
        'Selenium', 'JUnit', 'TestNG',
        'JIRA', 'Bugzilla', 'LoadRunner'
    ],
    'E-commerce': [
        'Shopify', 'Magento', 'WooCommerce'
    ],
    'Business Intelligence': [
        'DAX', 'M', 'Power Query',
        'Qlik Sense', 'Looker', 'Sisense'
    ],
    'Mobile Development': [
        'React Native', 'Flutter', 'Swift',
        'Kotlin', 'Ionic', 'Xamarin'
    ],
    'Embedded Systems': [
        'Arduino', 'Raspberry Pi', 'Microcontrollers',
        'Embedded C', 'Assembly', 'VHDL'
    ],
    'Blockchain': [
        'Ethereum', 'Smart Contracts', 'Hyperledger',
        'Solidity', 'Web3.js', 'Blockchain Security'
    ],
    'Game Development': [
        'Unity', 'Unreal Engine', 'CryEngine',
        'GameMaker Studio', 'Phaser', 'Godot Engine'
    ],
    'AR/VR Development': [
        'Unity 3D', 'UE4 (Unreal Engine 4)', 'ARKit',
        'ARCore', 'Vuforia', 'WebXR'
    ],
    'UI/UX Design': [
        'Adobe Illustrator', 'Adobe Photoshop', 'Adobe Premiere Pro',
        'After Effects', 'Sketch', 'InVision'
    ],
    'Digital Marketing': [
        'SEO', 'SEM', 'Google Analytics',
        'Facebook Ads', 'Instagram Ads', 'Email Marketing'
    ],
    'Customer Relationship Management (CRM)': [
        'Salesforce', 'HubSpot CRM', 'Zoho CRM',
        'Microsoft Dynamics CRM', 'Pipedrive', 'SugarCRM'
    ],
    'Project Management': [
        'Trello', 'Asana', 'Monday.com',
        'Basecamp', 'Wrike', 'MS Project'
    ],
    'Technical Support': [
        'Zendesk', 'Freshdesk', 'Help Scout',
        'Jira Service Desk', 'LiveChat', 'TeamViewer'
    ],
    'Content Management Systems (CMS)': [
        'WordPress', 'Drupal', 'Joomla',
        'Magento', 'Shopify', 'Wix'
    ],
}

# Inicializar janela principal
janela_principal = tk.Tk()
janela_principal.title("Análise de Currículo")
janela_principal.geometry("400x200")

# Função para enviar arquivo do currículo
def enviar_arquivo():
    # Abrir caixa de diálogo para selecionar o arquivo
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*")])

    if arquivo:
        # Exibir janela de seleção de habilidades
        selecionar_habilidades(arquivo)

# Função para selecionar habilidades
def selecionar_habilidades(arquivo):
    # Fechar janela principal
    janela_principal.withdraw()

    # Criar janela de seleção de habilidades
    janela_habilidades = tk.Toplevel()
    janela_habilidades.title("Selecionar Habilidades")

    # Frame para habilidades
    frame_habilidades = tk.Frame(janela_habilidades)
    frame_habilidades.pack(pady=20)

    # Criar um canvas com barra de rolagem para as habilidades
    canvas = tk.Canvas(frame_habilidades)
    scrollbar = tk.Scrollbar(frame_habilidades, orient="vertical", command=canvas.yview)
    frame_checkbox = tk.Frame(canvas)

    frame_checkbox.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    checkboxes = []
    for area, habilidades_area in habilidades.items():
        lbl_area = tk.Label(frame_checkbox, text=area, font=('Arial', 12, 'bold'))
        lbl_area.pack(anchor='w', padx=20, pady=5)
        for habilidade in habilidades_area:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(frame_checkbox, text=habilidade, variable=var, onvalue=1, offvalue=0)
            checkbox.pack(anchor='w', padx=40, pady=2)
            checkboxes.append((var, habilidade))

    # Configurar canvas e scrollbar
    canvas.create_window((0, 0), window=frame_checkbox, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Botão para calcular porcentagem
    btn_calcular = tk.Button(janela_habilidades, text="Calcular Porcentagem", command=lambda: calcular_porcentagem(arquivo, checkboxes))
    btn_calcular.pack(pady=10)

    # Botão para fechar janela
    btn_fechar = tk.Button(janela_habilidades, text="Fechar", command=fechar_janela)
    btn_fechar.pack(pady=10)

    # Ajustar tamanho da janela de habilidades
    janela_habilidades.update_idletasks()
    janela_habilidades.geometry(f"{frame_habilidades.winfo_reqwidth()}x{frame_habilidades.winfo_reqheight()}")

    # Exibir janela de habilidades
    janela_habilidades.mainloop()

# Função para calcular porcentagem do currículo
def calcular_porcentagem(arquivo, checkboxes):
    # Ler o texto do currículo do arquivo PDF
    try:
        text_archive = textract.process(arquivo)
        text_decoded = text_archive.decode('utf-8')
        text_corrected = ftfy.fix_text(text_decoded)
    except Exception as e:
        messagebox.showerror("Erro ao processar arquivo", f"Não foi possível ler o arquivo: {str(e)}")
        return

    # Armazenar texto corrigido em uma variável
    texto_curriculo = text_corrected.lower()

    # Inicializar lista para armazenar habilidades selecionadas
    habilidades_selecionadas = []

    # Percorrer checkboxes para verificar quais estão marcados
    for var, habilidade in checkboxes:
        if var.get() == 1:
            habilidades_selecionadas.append(habilidade)

    # Calcular porcentagem de habilidades encontradas no currículo
    total_habilidades = len(habilidades_selecionadas)
    if total_habilidades > 0:
        total_encontradas = sum(1 for habilidade in habilidades_selecionadas if habilidade.lower() in texto_curriculo)

        # Se todas as habilidades selecionadas estiverem no currículo, a porcentagem é 
        if total_encontradas == total_habilidades:
            porcentagem = 100.0
        else:
            porcentagem = (total_encontradas / total_habilidades) * 100

        # Exibir mensagem com a porcentagem
        messagebox.showinfo("Porcentagem do Currículo", f"A porcentagem do currículo é de {porcentagem:.2f}%")
    else:
        # Exibir mensagem se nenhuma habilidade estiver selecionada
        messagebox.showwarning("Nenhuma habilidade selecionada", "Por favor, selecione pelo menos uma habilidade para calcular a porcentagem.")

# Função para fechar janela de habilidades
def fechar_janela():
    janela_principal.deiconify()

# Botão para enviar arquivo
btn_enviar_arquivo = tk.Button(janela_principal, text="Enviar Arquivo", command=enviar_arquivo)
btn_enviar_arquivo.pack(pady=50)

# Iniciar loop da aplicação
janela_principal.mainloop()
