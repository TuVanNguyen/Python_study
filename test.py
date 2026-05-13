def minReorder(self, n: int, connections: List[List[int]]) -> int:
    reroutes = 0
    adjacent = {n: dict() for n in range(n)}
    seen = set()

    for route in connections:
        adjacent[route[0]][route[1]] = 0
        adjacent[route[1]][route[0]] = 1

    def dfs(city):
        nonlocal reroutes
        if city in seen:
            return
        seen.add(city)
        for city_2, direction in adjacent[city].items():
            if city_2 not in seen and direction == 0:
                reroutes += 1
            dfs(city_2)                

    dfs(0)
    return reroutes




