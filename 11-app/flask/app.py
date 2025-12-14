from flask import Flask, render_template, session, redirect, url_for

from shop.use_cases.plugin_recognition import PluginService
from shop.use_cases.shop_tree_view import TreeView

app = Flask(__name__)
app.config['APP_NAME'] = 'webshop'
app.config['DATASOURCE_GROUP'] = 'shop.datasource'
app.secret_key = 'super_secret_random_string_for_session'

plugin_service = PluginService()
plugin_service.load_plugins(app.config['DATASOURCE_GROUP'])


@app.route('/')
def index():
    datasource_plugins = plugin_service.plugins[app.config['DATASOURCE_GROUP']]
    return render_template('index.html', title='Index', datasource_plugins=datasource_plugins)

@app.route('/plugin/datasource/<id>')
def datasource_plugin(id: str):
    session['selected_datasource_plugin'] = id
    return redirect(url_for('index'))

@app.route('/layout/tree')
def tree_layout():
    selected_plugin = session['selected_datasource_plugin']
    datasource_plugins = plugin_service.plugins[app.config['DATASOURCE_GROUP']]

    tree_view = TreeView(plugin_service)
    header, body = tree_view.render(selected_plugin)

    return render_template('shop-tree-layout.html',
                           title='Shop tree layout',
                           datasource_plugins=datasource_plugins,
                           tree_view_header=header,
                           tree_view_body=body)


if __name__ == '__main__':
    app.run()
