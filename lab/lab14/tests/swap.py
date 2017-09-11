test = {
  'name': 'swap',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (swap (list 1 2 3 4))
          (2 1 4 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (swap (list 1 2 3 4 5))
          (2 1 4 3 5)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (swap '()))
          ()
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab14)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
