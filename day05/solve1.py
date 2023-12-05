import functools; print(
    (lambda chunks: 
        (lambda seeds, maps: 
            min(functools.reduce(  # apply all maps to seeds
                lambda state, current_map: [
                    ([
                        value + map_entry[0] - map_entry[1]
                        for map_entry in current_map
                        if value >= map_entry[1] and value < map_entry[1] + map_entry[2]
                    ] or [value])[0]
                    for value in state
                ],
                maps,
                seeds
            ))
        )(chunks[0][0], chunks[1:])
    )(
        (lambda chunks: [
            [
                [int(i) for i in row.split()] 
                for row in chunk.split(":")[1].strip().split('\n')
            ]
            for chunk in chunks
        ])(open("input.txt").read().split('\n\n'))
    )
)