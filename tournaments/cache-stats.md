# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0029-20261011-130205)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 164 | 1731597 | 1009664 | 58.3% | 58.4% |
| GPT-6.1 Sol | 82 | 1655394 | 1474816 | 89.1% | 90.2% |
| Sonnet 5.5 | 90 | 1477316 | 1378239 | 93.3% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7735 | 86532804 | 44352512 | 51.3% | 51.2% |
| GPT-6.1 Sol | 6158 | 179145362 | 166886016 | 93.2% | 93.6% |
| Sonnet 5.5 | 6316 | 138391862 | 132087309 | 95.4% | 96.1% |
