from ipyaggrid import Grid

# Example data
teams = []  # replace with actual DataFrame or list of dicts

grid_options = {
    'rowSelection': 'multiple',
    'editable': False,
    'suppressRowClickSelection': False,
}

column_defs = [
    {'headerName': 'Name', 'field': 'name'},
    {'headerName': 'ID', 'field': 'id'},
    {'headerName': 'Jersey', 'field': 'jersey'},
]

aggrid_widget = Grid(
    grid_data=teams,
    grid_options=grid_options,
    column_defs=column_defs,  # Correct argument name
    quick_filter=True,
    sync_on_edit=True,
)
