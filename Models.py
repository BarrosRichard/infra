from infra.config import Database
from sqlalchemy import Table

#  contrução de modelos prontos
class ConfigSite(Database().base):
    __table__ = Table('config_site', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class ConfigTemplate(Database().base):
    __table__ = Table('config_template', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Roles(Database().base):
    __table__ = Table('roles', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class SeleniumKeys(Database().base):
    __table__ = Table('selenium_keys', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Apis(Database().base):
    __table__ = Table('sit_apis', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Categorias(Database().base):
    __table__ = Table('sit_categorias', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Cliente(Database().base):
    __table__ = Table('sit_cliente', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Computers(Database().base):
    __table__ = Table('sit_computers', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Configuracao(Database().base):
    __table__ = Table('sit_configuracao', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class CronRelacao(Database().base):
    __table__ = Table('sit_cron_relacao', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Feedback(Database().base):
    __table__ = Table('sit_feedback', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class HorariosAtualizacao(Database().base):
    __table__ = Table('sit_horarios_atualizacao', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class IfoodMerchants(Database().base):
    __table__ = Table('sit_ifood_merchants', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class LinksBI(Database().base):
    __table__ = Table('sit_links_bi', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Local(Database().base):
    __table__ = Table('sit_local', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Logs(Database().base):
    __table__ = Table('sit_logs', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class LogsFull(Database().base):
    __table__ = Table('sit_logs_full', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Notificacoes(Database().base):
    __table__ = Table('sit_notificacoes', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class NotificacoesVisualizadas(Database().base):
    __table__ = Table('sit_notificacoes_visualizadas', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class RPALogs(Database().base):
    __table__ = Table('sit_rpa_logs', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Slide(Database().base):
    __table__ = Table('sit_slide', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Stack(Database().base):
    __table__ = Table('sit_stack_empresas', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class StatusBI(Database().base):
    __table__ = Table('sit_status_bi', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class StatusBILast(Database().base):
    __table__ = Table('sit_status_bi_last', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Users(Database().base):
    __table__ = Table('users', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

class Empresas(Database().base):
    __table__ = Table('sit_empresas', Database().base.metadata,
                    autoload=True, autoload_with=Database().engine)

"""
  ___
                               ,-""   `.
                             ,'  _   e )`-._
                            /  ,' `-._<.===-' (QUACK!)
                           /  /
                          /  ;
              _.--.__    /   ;
 (`._    _.-""       "--'    |
 <_  `-""                     \
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
     Patoda vida    `
"""