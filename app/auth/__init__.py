You're using code navigation to jump to definitions or references.
Learn more or give us feedback
from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views,forms