from bottle import route, run, template, static_file

frettir = [

    {
        'fyrirsogn': 'Tvítugur maður á enn eftir að læra að setja á sig skó',
        'texti': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        'mynd': 'frett1.jpg',
        'email': 'gmj@gmail.com'

    },

    {
        'fyrirsogn': 'Fjölmenn mótmæli í Aþenu vegna Makedóníu-deilunnar',
        'texti': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        'mynd': 'frett2.jpg',
        'email': 'gmj@gmail.com'

    },

    {
        'fyrirsogn': 'Var fluttur meðvitundarlaus á slysadeild eftir árás þriggja manna',
        'texti': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        'mynd': 'frett3.jpg',
        'email': 'gmj@gmail.com'

    },

    {
        'fyrirsogn': 'Sex manna fjölskylda í Hafnarfirði á sjö husky hunda',
        'texti': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
        'mynd': 'frett4.jpg',
        'email': 'gmj@gmail.com'

    },
]

@route('/')
def index():
    return template('verk3')

@route('/a')
def lidurA():
    return template('lidurA')

@route('/kt/<kennitala>')
def kt(kennitala):
    return template('kt', kennitala=kennitala)

@route('/b')
def lidurB():
    return template('index', frettir=frettir)

@route('/frettir/<n>')
def frett(n):
    return template('frett', n=n, frettir=frettir)

#static file routing
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root ='./myfiles')

run()