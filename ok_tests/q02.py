test = {
  'name': 'Problem Set 5 q02',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(YoverL_50_alphaquarter, 3.7, atol=0.1) 
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(YoverL_50_alphathird, 4.8, atol=0.1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(YoverL_50_alphahalf, 11.0, atol=0.1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(YoverL_50_alphatwothirds, 57.2, atol=0.1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(YoverL_50_alphathreequarters, 297.7, atol=0.1)
          True
          """,
          'hidden': False,
          'locked': False
        }  
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
