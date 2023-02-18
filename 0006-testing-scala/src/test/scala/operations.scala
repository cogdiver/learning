import operations.sum._

import org.scalatest.funsuite.AnyFunSuite

class OperationsTest extends AnyFunSuite {

  test("sum 2 to 2 must return 4") {
    assert(sum2(2) == 4)
  }
  test("sum 3 to 2 must return 5") {
    assert(sum3(2) == 5)
  }
  test("sum 4 to 2 must return 6") {
    assert(sum4(2) == 6)
  }
}
