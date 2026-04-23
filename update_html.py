import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    r'<h2>Helados Caseros</h2>': r'<h2 data-i18n="app_title">Helados Caseros</h2>',
    r'<i class="fa-solid fa-house"></i> Principal': r'<i class="fa-solid fa-house"></i> <span data-i18n="nav_principal">Principal</span>',
    r'<i class="fa-solid fa-chart-line"></i> Ventas': r'<i class="fa-solid fa-chart-line"></i> <span data-i18n="nav_ventas">Ventas</span>',
    r'<i class="fa-solid fa-clipboard-list"></i> Pedidos': r'<i class="fa-solid fa-clipboard-list"></i> <span data-i18n="nav_pedidos">Pedidos</span>',
    r'<i class="fa-solid fa-cart-shopping"></i> Compras': r'<i class="fa-solid fa-cart-shopping"></i> <span data-i18n="nav_compras">Compras</span>',
    r'<i class="fa-solid fa-wallet"></i> Resumen de Cuentas': r'<i class="fa-solid fa-wallet"></i> <span data-i18n="nav_resumen">Resumen de Cuentas</span>',
    r'<i class="fa-solid fa-trash-can"></i> Papelera': r'<i class="fa-solid fa-trash-can"></i> <span data-i18n="nav_papelera">Papelera</span>',
    r'<h1>Resumen General</h1>': r'<h1 data-i18n="tab_principal_title">Resumen General</h1>',
    r'<p>Helados Vendidos \(Mes\)</p>': r'<p data-i18n="stat_helados">Helados Vendidos (Mes)</p>',
    r'<p>Pedidos Realizados \(Mes\)</p>': r'<p data-i18n="stat_pedidos_mes">Pedidos Realizados (Mes)</p>',
    r'<p>Pedidos Pendientes</p>': r'<p data-i18n="stat_pedidos_pendientes">Pedidos Pendientes</p>',
    r'<h3>Flujo del Mes Actual</h3>': r'<h3 data-i18n="chart_flujo_mes">Flujo del Mes Actual</h3>',
    r'<h3>Próximas Entregas</h3>': r'<h3 data-i18n="list_entregas">Próximas Entregas</h3>',
    r'<h1>Ventas</h1>': r'<h1 data-i18n="tab_ventas_title">Ventas</h1>',
    r'<p>Registro mensual de ventas directas\.</p>': r'<p data-i18n="tab_ventas_desc">Registro mensual de ventas directas.</p>',
    r'<i class="fa-solid fa-plus"></i> Nueva Venta': r'<i class="fa-solid fa-plus"></i> <span data-i18n="btn_nueva_venta">Nueva Venta</span>',
    r'<h1>Pedidos</h1>': r'<h1 data-i18n="tab_pedidos_title">Pedidos</h1>',
    r'<p>Gestión de encargos y entregas\.</p>': r'<p data-i18n="tab_pedidos_desc">Gestión de encargos y entregas.</p>',
    r'<i class="fa-solid fa-plus"></i> Nuevo Pedido': r'<i class="fa-solid fa-plus"></i> <span data-i18n="btn_nuevo_pedido">Nuevo Pedido</span>',
    r'<h1>Compras</h1>': r'<h1 data-i18n="tab_compras_title">Compras</h1>',
    r'<p>Registro de gastos e insumos por mes\.</p>': r'<p data-i18n="tab_compras_desc">Registro de gastos e insumos por mes.</p>',
    r'<i class="fa-solid fa-plus"></i> Nueva Compra': r'<i class="fa-solid fa-plus"></i> <span data-i18n="btn_nueva_compra">Nueva Compra</span>',
    r'<h1>Resumen de Cuentas</h1>': r'<h1 data-i18n="tab_resumen_title">Resumen de Cuentas</h1>',
    r'<p>Balance general de ingresos, gastos y ganancias\.</p>': r'<p data-i18n="tab_resumen_desc">Balance general de ingresos, gastos y ganancias.</p>',
    r'<h3>Evolución Anual</h3>': r'<h3 data-i18n="chart_evolucion">Evolución Anual</h3>',
    r'<h1>Papelera de Reciclaje</h1>': r'<h1 data-i18n="tab_papelera_title">Papelera de Reciclaje</h1>',
    r'<p>Registros eliminados recientemente\.</p>': r'<p data-i18n="tab_papelera_desc">Registros eliminados recientemente.</p>',
    r'<i class="fa-solid fa-dumpster"></i> Vaciar Papelera': r'<i class="fa-solid fa-dumpster"></i> <span data-i18n="btn_vaciar_papelera">Vaciar Papelera</span>',
    r'<h2>Registrar Venta</h2>': r'<h2 data-i18n="modal_venta_title">Registrar Venta</h2>',
    r'<label for="venta-fecha">Fecha</label>': r'<label for="venta-fecha" data-i18n="label_fecha">Fecha</label>',
    r'<label for="venta-cantidad">Cantidad Total de Helados</label>': r'<label for="venta-cantidad" data-i18n="label_cantidad">Cantidad Total de Helados</label>',
    r'>Cancelar</button>': r' data-i18n="btn_cancelar">Cancelar</button>',
    r'>Guardar</button>': r' data-i18n="btn_guardar">Guardar</button>',
    r'<h2>Registrar Compra</h2>': r'<h2 data-i18n="modal_compra_title">Registrar Compra</h2>',
    r'<label for="compra-producto">Producto/Insumo</label>': r'<label for="compra-producto" data-i18n="label_producto">Producto/Insumo</label>',
    r'<label for="compra-fecha">Fecha de Compra</label>': r'<label for="compra-fecha" data-i18n="label_fecha_compra">Fecha de Compra</label>',
    r'<label for="compra-lugar">Lugar de Compra</label>': r'<label for="compra-lugar" data-i18n="label_lugar_compra">Lugar de Compra</label>',
    r'<label for="compra-costo">Costo Total \(\$\)</label>': r'<label for="compra-costo" data-i18n="label_costo">Costo Total ($)</label>',
    r'<h2>Nuevo Encargo / Pedido</h2>': r'<h2 data-i18n="modal_pedido_title">Nuevo Encargo / Pedido</h2>',
    r'<label for="pedido-nombre">Nombre de la persona/entidad</label>': r'<label for="pedido-nombre" data-i18n="label_nombre">Nombre de la persona/entidad</label>',
    r'<label for="pedido-fecha">Fecha del encargo</label>': r'<label for="pedido-fecha" data-i18n="label_fecha_encargo">Fecha del encargo</label>',
    r'<label for="pedido-entrega">Fecha de entrega</label>': r'<label for="pedido-entrega" data-i18n="label_fecha_entrega">Fecha de entrega</label>',
    r'<label for="pedido-lugar">Lugar de entrega</label>': r'<label for="pedido-lugar" data-i18n="label_lugar_entrega">Lugar de entrega</label>',
    r'<h3 class="section-title">Sabores y Cantidades</h3>': r'<h3 class="section-title" data-i18n="title_sabores">Sabores y Cantidades</h3>',
    r'<label>Maracuy(á|ǭ)</label>': r'<label data-i18n="label_maracuya">Maracuyá</label>',
    r'<label>Mora</label>': r'<label data-i18n="label_mora">Mora</label>',
    r'<label>Pi(ñ|)a</label>': r'<label data-i18n="label_pina">Piña</label>',
    r'<label>Coco</label>': r'<label data-i18n="label_coco">Coco</label>',
    r'<label>Queso</label>': r'<label data-i18n="label_queso">Queso</label>',
    r'<label>Total Helados</label>': r'<label data-i18n="label_total_helados">Total Helados</label>',
    r'<label>Valor Helados \(\$\)</label>': r'<label data-i18n="label_valor_helados">Valor Helados ($)</label>',
    r'<label for="pedido-transporte">Valor Transporte \(\$\)</label>': r'<label for="pedido-transporte" data-i18n="label_valor_transporte">Valor Transporte ($)</label>',
    r'<label>Costo Total del Pedido</label>': r'<label data-i18n="label_costo_total_pedido">Costo Total del Pedido</label>',
    r'>Guardar Pedido</button>': r' data-i18n="btn_guardar_pedido">Guardar Pedido</button>',
    r'<h2 id="detalle-titulo">Detalles</h2>': r'<h2 id="detalle-titulo" data-i18n="modal_detalle_title">Detalles</h2>',
    r'<h2 style="margin-bottom: 1rem;">(¿Estás seguro\?|Estǭs seguro\?)</h2>': r'<h2 style="margin-bottom: 1rem;" data-i18n="modal_confirm_title">¿Estás seguro?</h2>',
    r'<p id="confirm-text" style="color: var\(--text-muted\); margin-bottom: 2rem;">(¿Estás seguro de que quieres eliminar el registro\?|Estǭs seguro de que quieres eliminar el registro\?)</p>': r'<p id="confirm-text" style="color: var(--text-muted); margin-bottom: 2rem;" data-i18n="modal_confirm_text">¿Estás seguro de que quieres eliminar el registro?</p>',
    r'>No, cancelar</button>': r' data-i18n="btn_no_cancelar">No, cancelar</button>',
    r'>(Sí|S), eliminar</button>': r' data-i18n="btn_si_eliminar">Sí, eliminar</button>'
}

for k, v in replacements.items():
    html = re.sub(k, v, html)

# Add the language toggle selector right after <main class="main-content">
lang_toggle = """
            <div class="lang-selector">
                <button id="lang-btn-es" class="lang-btn active" onclick="setLanguage('es')">ES</button>
                <button id="lang-btn-en" class="lang-btn" onclick="setLanguage('en')">EN</button>
            </div>
"""
html = html.replace('<main class="main-content">', f'<main class="main-content">{lang_toggle}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
