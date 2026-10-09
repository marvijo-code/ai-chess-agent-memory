# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0014-20261009-214817)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 165 | 1687987 | 832256 | 49.3% | 49.4% |
| GPT-6.1 Sol | 132 | 3838545 | 3619712 | 94.3% | 94.7% |
| Sonnet 5.5 | 114 | 2228837 | 2110638 | 94.7% | 95.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3479 | 37727922 | 17395968 | 46.1% | 46.0% |
| GPT-6.1 Sol | 3032 | 88612228 | 82292352 | 92.9% | 93.3% |
| Sonnet 5.5 | 3201 | 71618965 | 68438782 | 95.6% | 96.1% |
