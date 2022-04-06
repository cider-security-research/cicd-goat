pipelineJob('cov-reportcov') {
  environmentVariables {
    env('KEY', "-----BEGIN OPENSSH PRIVATE KEY-----\\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn\\nNhAAAAAwEAAQAAAYEAzKMQY9T7R2JBDjFuxCxQWxKI9Nf39EdewMpSYfgR4AslScEzJJX0\\nO3lfkq1jalL4zp066bFkU21M3p42hVgXnBrcVOR7JU3FiEFDw4qfE2CcJTXFHL4obAqFiy\\ncp6RxsIjRIoRz8zrBI57k8CyhqZK104xt79XDkWcDnA7lctBwq9Dq9vxsK8SqXvW4cJTu7\\nosoyMitO3RP3x0EYocsNNnTDNBj1JIMsfmSkOu503LFZqAuqhchKm7BcnpeOYT2qKRuFqv\\nBowklegCZRWZNWSVI1lGhUQQ3wDgEk0dqUPzHlOhDx4hNAeT/RXttllY+lxci00EFmjRs3\\nXXgculpXRs3cyC+T3Itn4rQoE5AV5191mIuwufozXCiGgFhOKfOmYe8ZHCcI09pmT2xZ9m\\nCpq5VharLKHR3ku4yy3NEYZrOcNvhIfSlkFCTYV5IKXr9VcS3f+KMNrBgvEF0tEqo3sy87\\n1bbUInjCTViMvCS8G2uFQlnvMRiW4+FNyCcSUqpBAAAFkAzpeAEM6XgBAAAAB3NzaC1yc2\\nEAAAGBAMyjEGPU+0diQQ4xbsQsUFsSiPTX9/RHXsDKUmH4EeALJUnBMySV9Dt5X5KtY2pS\\n+M6dOumxZFNtTN6eNoVYF5wa3FTkeyVNxYhBQ8OKnxNgnCU1xRy+KGwKhYsnKekcbCI0SK\\nEc/M6wSOe5PAsoamStdOMbe/Vw5FnA5wO5XLQcKvQ6vb8bCvEql71uHCU7u6LKMjIrTt0T\\n98dBGKHLDTZ0wzQY9SSDLH5kpDrudNyxWagLqoXISpuwXJ6XjmE9qikbharwaMJJXoAmUV\\nmTVklSNZRoVEEN8A4BJNHalD8x5ToQ8eITQHk/0V7bZZWPpcXItNBBZo0bN114HLpaV0bN\\n3Mgvk9yLZ+K0KBOQFedfdZiLsLn6M1wohoBYTinzpmHvGRwnCNPaZk9sWfZgqauVYWqyyh\\n0d5LuMstzRGGaznDb4SH0pZBQk2FeSCl6/VXEt3/ijDawYLxBdLRKqN7MvO9W21CJ4wk1Y\\njLwkvBtrhUJZ7zEYluPhTcgnElKqQQAAAAMBAAEAAAGAResRFosWr/UqNSc+qVhavENA+C\\ncyWQxpm4WFUGPp95rXSrPwPXfe0tNNjFght5pR2IZwMpihpr+ZnBaCmlzW9EdZMMhAKya/\\nbyadeJpMb9p6f1w31PJD7WZK6pifAT7s02L5zdKRri0dO89WbJmKgIujfFVPrTS9UM1QIT\\n2cJw3Yv0myuzEKNAxRfC+6/h3CpoRfUjTp5S+FYVcki2NNSGXsrEg6uhb3hNfuJRSEaUNP\\nVtNlmAAvPbKscqNlymO+u1EP9W34UDRCNqGdLZxFs651a50qmmQvTAMYHCOTFUE3ChGnEI\\nBGLEtsOkYKlEnQg5qQIHKLJExH0a2b0fVFrGK7dcVK3kc7xLgGwvxuFvKl4DeMgCX5q85g\\n02Mu9Odcsio7t6Go6sXTiB3V/Idbzcp3zbO3B76AQDzhjzTtGYONPR+aDthfnJIJhyxRJg\\nmaE9IHWIpiWe0gzjnSs4HBGqF0F6Rr/XIbjN/53wBmyMO6eVq2wAHbRu/NEgisctfhAAAA\\nwQCuImeTnL8fGofb3jTAYeckTPiUsM2RsshSbwlZaX3TR4TWNu0mcc94hYButIcG2SMVXc\\nF4i9jl6cdgAff43uoPy8GKiGc9jF4eylky4c4fgw7EzbtFMPmpFnteA/Oh0SxlxhmUDVHU\\nmxRkssDSI7Zif6z2KaT3Z9yK92y/265Sm2gkIUshm2BNplgssCdIkNtqZaePBmHr6/09oJ\\nhRSJmmgkesx7TJ9BqVuuiZdn3E71XNHsbBOyD08cLrZEoNtjkAAADBAPKW8trXU/H85DOl\\nm9ZN6VGIbnFgtItUN8ntsS2srJ3N5VyfNiGg3pM3p0pWtOmSgjTPjrbeEtb44O73/0z38W\\nHfzphsbgHg0TVVEFN28N7yLHYpMRkLPz70h/RIBLRmaZrIYKuQ+KgSAPAKydnHaV8JJV75\\nubOTb6IEGcR9jFOjwnEe+7pC3AZOwdkstQqCM8mUWUywqKVQ2j4iFeCWyGc2jWGq3tpT9C\\noRq1Wiv56KO8IJGHfIAczKyTyLwrxgxwAAAMEA1/MFbll+7fir7eNaJuD2nhvOVq0BlBTj\\nKLOlCgZnBsWhh+uL+/7hzPQJdG9qZyjk2nkPeUzgwgfbtsjDhp18d1rN+ZvP7mXgtzS02K\\nownCDcQz+weO/BhAFFl6IkDPB0XnC8oC0PNKs9Pp9SKlkiDtTKcvFCOBaq5LOn3XFQdaZR\\nlFAeCtpLFZd1aqozL+WxdhJ+OlUMWexAHNVInX3vM245R2hiSEHJfCMKwKmdQ2nkpyCjMz\\nnFX2YLEFe9BqS3AAAAF2FzaUBBc2FmLkdyZWVuaG9sdHMtTUJQAQID\\n-----END OPENSSH PRIVATE KEY-----\\n")
  }
  definition {
    cpsScm {
      scm {
        git {
          remote {
            url('http://gitea:3000/Cov/march-hare.git')
          }
          branch('main')
        }
      }
      scriptPath('Jenkinsfile')
    }
  }
  triggers {
    GenericTrigger {
      causeString('Caused by $x_gitea_event')
      token('6AE44837-0E0C-4970-9A40-8C780E6FFBA1')
      regexpFilterExpression('^(pushNone|pull_requestopened)$')
      regexpFilterText('$x_gitea_event$action')
      genericHeaderVariables {
        genericHeaderVariable {
          key('x-gitea-event')
          regexpFilter('')
        }
      }
      genericVariables {
        genericVariable {
          key('action')
          expressionType('JSONPath')
          value('$.action')
          defaultValue('None')
        }
        genericVariable {
          key('title')
          expressionType('JSONPath')
          value('$.pull_request.title')
        }
      }
    }
  }
}