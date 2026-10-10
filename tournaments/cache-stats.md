# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 256 | 2847010 | 1777152 | 62.4% | 62.6% |
| GPT-6.1 Sol | 208 | 5849351 | 5435136 | 92.9% | 93.4% |
| Sonnet 5.5 | 196 | 4263003 | 4059747 | 95.2% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6151 | 68350481 | 34027520 | 49.8% | 49.7% |
| GPT-6.1 Sol | 4982 | 143515822 | 133497344 | 93.0% | 93.5% |
| Sonnet 5.5 | 5228 | 115692306 | 110495450 | 95.5% | 96.1% |
