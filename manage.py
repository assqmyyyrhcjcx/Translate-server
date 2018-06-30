#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from models import User

# 类似shell命令
manage = Manager(app)

# 数据迁移，让app与db绑定
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manage中
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()