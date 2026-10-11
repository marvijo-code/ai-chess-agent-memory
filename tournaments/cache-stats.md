# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0029-20261011-130205)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 87 | 882334 | 531456 | 60.2% | 60.4% |
| GPT-6.1 Sol | 44 | 818571 | 737280 | 90.1% | 92.1% |
| Sonnet 5.5 | 59 | 944848 | 882206 | 93.4% | 94.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7658 | 85683541 | 43874304 | 51.2% | 51.2% |
| GPT-6.1 Sol | 6120 | 178308539 | 166148480 | 93.2% | 93.6% |
| Sonnet 5.5 | 6285 | 137859394 | 131591276 | 95.5% | 96.1% |
