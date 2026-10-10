# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0015-20261010-001334)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 197 | 2357683 | 1228288 | 52.1% | 52.1% |
| GPT-6.1 Sol | 125 | 3393326 | 3169792 | 93.4% | 93.8% |
| Sonnet 5.5 | 133 | 2853630 | 2719385 | 95.3% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3804 | 41493522 | 19347712 | 46.6% | 46.5% |
| GPT-6.1 Sol | 3255 | 95011117 | 88296960 | 92.9% | 93.4% |
| Sonnet 5.5 | 3427 | 76476588 | 73073167 | 95.5% | 96.1% |
