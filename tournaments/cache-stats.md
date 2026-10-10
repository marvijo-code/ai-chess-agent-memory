# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0015-20261010-001334)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 248 | 2827984 | 1401728 | 49.6% | 49.5% |
| GPT-6.1 Sol | 186 | 5618013 | 5317632 | 94.7% | 95.0% |
| Sonnet 5.5 | 193 | 4286980 | 4102393 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3855 | 41963823 | 19521152 | 46.5% | 46.4% |
| GPT-6.1 Sol | 3316 | 97235804 | 90444800 | 93.0% | 93.5% |
| Sonnet 5.5 | 3487 | 77909938 | 74456175 | 95.6% | 96.1% |
