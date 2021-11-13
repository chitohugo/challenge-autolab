import json

from api.model import Pokemon


class PokemonServices:
    @classmethod
    def get_all(cls, page, limit):
        result = Pokemon.get_all(page, limit)
        return result

    @classmethod
    def get_filters(cls, **params):
        filter_fields = {}
        _order_by = Pokemon.id.asc
        if "filters" in params:
            filter_fields = json.loads(params.get("filters"))
        if "sort" in params:
            sort_field = params.get("sort")
            sort = sort_field.split(":")
            field = sort[0]
            direction = sort[1]
            _order = getattr(Pokemon, field)
            _order_by = getattr(_order, direction)
        page = int(params.get("page")) if "page" in params else None
        per_page = int(params.get("limit")) if "limit" in params else None
        result = Pokemon.get_filters(filter_fields, _order_by, page, per_page)
        return result
