import web

# Url mapping
urls = (
    '/', 'index',
    '/index', 'index',
    '/register','register',
    '/login', 'login', 
    '/register', 'register',
)

# Global vars
global_vars = {
    'username':'Arashi',
}


#  Templates
render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index(globals = global_vars)

class register:
    def GET(self):
        return render.register("Register", globals = global_vars)

class login:
    def GET(self):
        return render.login("Login", globals = global_vars)
#
# class register:
#     def POST(self):
#
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True;
    app.run()
