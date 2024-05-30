object cap5 {



    // Function currying
    trait TaxStrategy { def taxIt(product: String): Double }
    val taxIt: (TaxStrategy, String) => Double = (s, p) => s.taxIt(p)
    taxIt.curried
    class TaxFree extends TaxStrategy { override def taxIt(product: String) = 0.0 }
    val taxFree = taxIt.curried(new TaxFree)
    taxFree("someProduct")

}


// ADT
object ADT {
    sealed trait Account
    case class CheckingAccount(accountId: String) extends Account
    case class SavingAccount(accountId: String, limit: Double) extends Account
    case class PremiumAccount(corporateId: String, accountHolder: String) extends Account

    def printAccountDetails(account: Account): Unit = account match {
        case CheckingAccount(accountId) => println("Account id " + accountId)
        case SavingAccount(accountId, limit) => println("Account id " + accountId + " , " + limit)
    }
}

// Why does functional programming matter
def sumar1(v: Int) = { println(v); v + 1 }
def sumar2(v: Int) = { println(v); v + 2 }
def sumar3(v: Int) = { println(v); v + 3 }

def sumar3andThen = sumar1 andThen sumar2
def sumar6andThen = sumar1 andThen sumar2 andThen sumar3

def sumar3compose = sumar1 compose sumar2
def sumar6compose = sumar1 compose sumar2 compose sumar3
