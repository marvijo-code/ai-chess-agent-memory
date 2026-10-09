# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0007-20261009-031124)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 67 | 584782 | 225152 | 38.5% | 38.1% |
| GPT-6.1 Sol | 78 | 2121011 | 1936000 | 91.3% | 92.1% |
| Sonnet 5.5 | 60 | 933867 | 870185 | 93.2% | 94.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1771 | 19664316 | 9059328 | 46.1% | 46.0% |
| GPT-6.1 Sol | 1452 | 42387710 | 39535360 | 93.3% | 93.7% |
| Sonnet 5.5 | 1602 | 36734069 | 35163796 | 95.7% | 96.2% |
