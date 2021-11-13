import json

from api.model import Pokemon


class PokemonServices:
    @classmethod
    def get_all(cls):
        result = Pokemon.get_all()
        return result

    @classmethod
    def get_filters(cls, **params):
        filter_fields = {}
        _order_by = Pokemon.id.asc
        if "filter" in params:
            filter_fields = json.loads(params.get("filter"))
        if "sort" in params:
            sort_field = params.get("sort")
            sort = sort_field.split(":")
            field = sort[0]
            direction = sort[1]
            _order = getattr(Pokemon, field)
            _order_by = getattr(_order, direction)

        result = Pokemon.get_filters(filter_fields, _order_by)
        return result
