# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0024-20261011-001419)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 39 | 341147 | 165888 | 48.6% | 48.4% |
| GPT-6.1 Sol | 23 | 407119 | 372736 | 91.6% | 92.2% |
| Sonnet 5.5 | 24 | 330599 | 303666 | 91.9% | 93.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6227 | 69177278 | 34440192 | 49.8% | 49.7% |
| GPT-6.1 Sol | 5005 | 143922941 | 133870080 | 93.0% | 93.5% |
| Sonnet 5.5 | 5268 | 116383812 | 111144574 | 95.5% | 96.1% |
