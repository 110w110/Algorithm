import Foundation

func solution(_ s:String) -> [Int] {
    var result : [Int] = []
    var dict: [Character : Int] = [:]
    for i in 0..<s.count {
        if dict[s[i]] == nil {
            result.append(-1)
            dict[s[i]] = i
        } else {
            result.append(i - dict[s[i]]!)
            dict[s[i]] = i
        }
    }
    return result
}

extension String {
    subscript(_ i: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: i)]
    }
    subscript(_ r: Range<Int>) -> String {
        let s = self.index(self.startIndex, offsetBy: r.startIndex)
        let e = self.index(self.endIndex, offsetBy: r.endIndex)
        return String(self[s..<e])
    }
}