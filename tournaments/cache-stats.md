# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0025-20261011-030533)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 162 | 2466184 | 1332224 | 54.0% | 54.0% |
| GPT-6.1 Sol | 60 | 1418466 | 1301760 | 91.8% | 92.2% |
| Sonnet 5.5 | 98 | 2180071 | 2089308 | 95.8% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6625 | 74362783 | 37413376 | 50.3% | 50.3% |
| GPT-6.1 Sol | 5256 | 151691890 | 141144448 | 93.0% | 93.5% |
| Sonnet 5.5 | 5542 | 122453500 | 116945337 | 95.5% | 96.1% |
